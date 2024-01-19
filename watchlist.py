from main import *


@app.get("/profiles/{profile_id}/watchlist", response_model=List[WatchlistRead])
def read_watchlist_by_profile(
        *,
        session: Session = Depends(get_session),
        profile_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        watchlists = session.query(Watchlist).filter(Watchlist.profile_id == profile_id).all()
        if not watchlists:
            raise HTTPException(status_code=404, detail="No watchlists found")

        if accept and "application/xml" in accept:
            # watchlist_data = {"watchlist": [watchlist.dict() for watchlist in watchlists]}
            # xml_content = xmltodict.unparse(watchlist_data, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=watchlist_to_xml_string(watchlists), media_type="application/xml")
        else:
            return watchlists


@app.post("/watchlist/movie", response_model=WatchlistRead)
def add_movie_to_watchlist(
        *,
        session: Session = Depends(get_session),
        watchlist_create: WatchlistCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        movie_id = watchlist_create.movie_id
        if not session.query(Movie).filter(Movie.movie_id == movie_id).first():
            raise HTTPException(status_code=404, detail="Movie not found")

        profile_id = watchlist_create.profile_id
        if not session.query(Profile).filter(Profile.profile_id == profile_id).first():
            raise HTTPException(status_code=404, detail="Profile not found")

        watchlist = Watchlist(**watchlist_create.dict())
        session.add(watchlist)
        session.commit()
        return watchlist


@app.put("/watchlist/{watchlist_id}", response_model=WatchlistRead)
def update_watchlist(
        *,
        session: Session = Depends(get_session),
        watchlist_id: int,
        watchlist_update: WatchlistCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        watchlist = session.get(Watchlist, watchlist_id)
        if not watchlist:
            raise HTTPException(status_code=404, detail="Watchlist not found")

        for field, value in watchlist_update.dict().items():
            setattr(watchlist, field, value)

        session.commit()
        return watchlist


@app.delete("/watchlist/{watchlist_id}")
def delete_profile(*, session: Session = Depends(get_session),
                   watchlist_id: int,
                   api_key_header: Optional[str] = Depends(api_key_header)
                   ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        watchlist = session.get(Watchlist, watchlist_id)
        if not watchlist:
            raise HTTPException(status_code=404, detail="Watchlist not found")

        session.delete(watchlist)
        session.commit()
        return {"message": "Watchlist deleted successfully"}