from main import *


@app.get("/episodes/{episode_id}/subtitles", response_model=List[SubtitleRead])
def read_subtitles_by_episode(
        *,
        session: Session = Depends(get_session),
        episode_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        subtitles = session.query(Subtitle).filter(Subtitle.episode_id == episode_id).all()
        if not subtitles:
            raise HTTPException(status_code=404, detail="No subtitles found")

        if accept and "application/xml" in accept:
            # subtitles_data = {"subtitle": [subtitle.dict() for subtitle in subtitles]}
            # xml_content = xmltodict.unparse(subtitles_data, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=subtitle_to_xml_string(subtitles), media_type="application/xml")
        else:
            return subtitles


@app.post("/episodes/{episode_id}/subtitles", response_model=SubtitleRead)
def create_subtitle_for_episode(
    *,
    session: Session = Depends(get_session),
    episode_id: int,
    subtitle_create: SubtitleCreate,
    api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        episode = session.get(Episode, episode_id)
        if not episode:
            raise HTTPException(status_code=404, detail="Episode not found")

        subtitle_data = subtitle_create.dict()
        subtitle_data["episode_id"] = episode_id

        subtitle = Subtitle(**subtitle_data)
        session.add(subtitle)
        session.commit()
        return subtitle


@app.post("/movies/{movie_id}/subtitles", response_model=SubtitleRead)
def create_subtitle_for_movie(
    *,
    session: Session = Depends(get_session),
    movie_id: int,
    subtitle_create: SubtitleCreate,
    api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        movie = session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

        subtitle_data = subtitle_create.dict()
        subtitle_data["movie_id"] = movie_id

        subtitle = Subtitle(**subtitle_data)
        session.add(subtitle)
        session.commit()
        return subtitle


@app.get("/movies/{movie_id}/subtitles", response_model=List[SubtitleRead])
def read_subtitles_by_movie(
        *,
        session: Session = Depends(get_session),
        movie_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        subtitles = session.query(Subtitle).filter(Subtitle.movie_id == movie_id).all()
        if not subtitles:
            raise HTTPException(status_code=404, detail="No subtitles found")

        if accept and "application/xml" in accept:
            # subtitles_data = {"subtitle": [subtitle.dict() for subtitle in subtitles]}
            # xml_content = xmltodict.unparse(subtitles_data, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=subtitle_to_xml_string(subtitles), media_type="application/xml")
        else:
            return subtitles


@app.put("/subtitles/{subtitle_id}", response_model=SubtitleRead)
def update_subtitle(
        *,
        session: Session = Depends(get_session),
        subtitle_id: int,
        subtitle_update: SubtitleCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        subtitle = session.get(Subtitle, subtitle_id)
        if not subtitle:
            raise HTTPException(status_code=404, detail="Subtitle not found")

        for field, value in subtitle_update.dict().items():
            setattr(subtitle, field, value)

        session.commit()
        return subtitle


@app.delete("/subtitles/{subtitle_id}")
def delete_subtitle(*, session: Session = Depends(get_session),
                    subtitle_id: int,
                    api_key_header: Optional[str] = Depends(api_key_header)
                    ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        subtitle = session.get(Subtitle, subtitle_id)
        if not subtitle:
            raise HTTPException(status_code=404, detail="Subtitle not found")

        session.delete(subtitle)
        session.commit()
        return {"message": "Subtitle deleted successfully"}