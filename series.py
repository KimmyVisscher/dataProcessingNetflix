from main import *


@app.get("/series", response_model=List[SerieRead])
def read_series(*, session: Session = Depends(get_session),
                api_key_header: Optional[str] = Depends(api_key_header),
                accept: Optional[str] = Header(None)
                ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        series = session.query(Serie).all()
        if not series:
            raise HTTPException(status_code=404, detail="No series found")

        if accept and "application/xml" in accept:
            return Response(content=series_to_xml_string(series), media_type="application/xml")
        else:
            return series


@app.get("/series/{serie_id}", response_model=SerieRead)
def read_series(*, session: Session = Depends(get_session),
                serie_id: int,
                api_key_header: Optional[str] = Depends(api_key_header),
                accept: Optional[str] = Header(None)
                ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        serie = session.get(Serie, serie_id)
        if not serie:
            raise HTTPException(status_code=404, detail="No series found")

        if accept and "application/xml" in accept:
            return Response(content=series_to_xml_string([serie]), media_type="application/xml")
        else:
            return serie


@app.get("/episodes/{episode_id}", response_model=EpisodeRead)
def read_episode(*, session: Session = Depends(get_session),
                episode_id: int,
                api_key_header: Optional[str] = Depends(api_key_header),
                accept: Optional[str] = Header(None)
                ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        episode = session.get(Episode, episode_id)
        if not episode:
            raise HTTPException(status_code=404, detail="Episode not found")

        if accept and "application/xml" in accept:
            return Response(content=episode_to_xml_string([episode]), media_type="application/xml")
        else:
            return episode


@app.get("/series/{serie_id}/episodes", response_model=List[EpisodeRead])
def read_episodes_by_serie(
    *,
    session: Session = Depends(get_session),
    serie_id: int,
    api_key_header: Optional[str] = Depends(api_key_header),
    accept: Optional[str] = Header(None),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        serie = session.get(Serie, serie_id)
        if not serie:
            raise HTTPException(status_code=404, detail="Serie not found")

        episodes = session.query(Episode).filter(Episode.serie_id == serie_id).all()
        if not episodes:
            raise HTTPException(status_code=404, detail="No episodes found for the serie")

        if accept and "application/xml" in accept:
            return Response(content=episode_to_xml_string(episodes), media_type="application/xml")
        else:
            return episodes


@app.get("/series/genre/{genre}", response_model=List[SerieRead])
def read_series_by_genre(
        *,
        session: Session = Depends(get_session),
        genre: Genre,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        series = session.query(Serie).filter(Serie.serie_genre.any(genre=genre.value)).all()
        if not series:
            raise HTTPException(status_code=404, detail="No series found")

        if accept and "application/xml" in accept:
            return Response(content=series_to_xml_string(series), media_type="application/xml")
        else:
            return series


@app.get("/series/{serie_id}/genres", response_model=List[GenresRead])
def read_genre_by_serie(
        *,
        session: Session = Depends(get_session),
        serie_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        genres = session.query(Genres).filter(Genres.serie_id == serie_id).all()
        if not genres:
            raise HTTPException(status_code=404, detail="No genres found")

        if accept and "application/xml" in accept:
            return Response(content=genre_to_xml_string(genres), media_type="application/xml")
        else:
            return genres


@app.post("/series")
def create_serie(*, session: Session = Depends(get_session),
                 serie_create: SerieCreate,
                 api_key_header: Optional[str] = Depends(api_key_header)
                 ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        serie = Serie(**serie_create.dict())
        session.add(serie)
        session.commit()
        return return_created()


@app.post("/episodes")
def create_episode(
        *,
        session: Session = Depends(get_session),
        episode_create: EpisodeCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        serie_id = episode_create.serie_id
        if not session.query(Serie).filter(Serie.serie_id == serie_id).first():
            raise HTTPException(status_code=404, detail="Serie not found")

        episode = Episode(**episode_create.dict())
        session.add(episode)
        session.commit()
        return return_created()


@app.put("/series/{serie_id}", response_model=SerieRead)
def update_serie(
        *,
        session: Session = Depends(get_session),
        serie_id: int,
        serie_update: SerieCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        serie = session.get(Serie, serie_id)
        if not serie:
            raise HTTPException(status_code=404, detail="Serie not found")

        for field, value in serie_update.dict().items():
            setattr(serie, field, value)

        session.commit()
        return serie


@app.put("/episodes/{episode_id}", response_model=EpisodeRead)
def update_episode(
        *,
        session: Session = Depends(get_session),
        episode_id: int,
        episode_update: EpisodeCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        episode = session.get(Episode, episode_id)
        if not episode:
            raise HTTPException(status_code=404, detail="Episode not found")

        for field, value in episode_update.dict().items():
            setattr(episode, field, value)

        session.commit()
        return episode


@app.delete("/series/{serie_id}")
def delete_series(*, session: Session = Depends(get_session),
                  serie_id: int,
                  api_key_header: Optional[str] = Depends(api_key_header)
                  ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        serie = session.get(Serie, serie_id)
        if not serie:
            raise HTTPException(status_code=404, detail="Series not found")

        session.delete(serie)
        session.commit()
        return return_deleted()


@app.delete("/episodes/{episode_id}")
def delete_episode(*, session: Session = Depends(get_session),
                   episode_id: int,
                   api_key_header: Optional[str] = Depends(api_key_header)
                   ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        episode = session.get(Episode, episode_id)
        if not episode:
            raise HTTPException(status_code=404, detail="Episode not found")

        session.delete(episode)
        session.commit()
        return return_deleted()


@app.get("/series/{serie_id}/imdb")
def get_imdb_rating_by_serie(serie_id: int,
                    session: Session = Depends(get_session),
                    api_key_header: Optional[str] = Depends(api_key_header),
                    accept: Optional[str] = Header(None)
                    ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        serie = session.get(Serie, serie_id)
        if not serie:
            raise HTTPException(status_code=404, detail="Serie not found")

        title = serie.serie_name
        omdb_url = f"http://www.omdbapi.com/?apikey={omdbkey}&t={title}"

        response = requests.get(omdb_url)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch IMDb rating")

        imdb_data = response.json()
        imdb_rating = imdb_data.get("imdbRating")
        if not imdb_rating:
            raise HTTPException(status_code=500, detail="IMDb rating not available")

        if accept and "application/xml" in accept:
            return PlainTextResponse(content=f"<imdbRating>{imdb_rating}</imdbRating>", media_type="application/xml")

        else:
            return {"imdbRating": imdb_rating}


@app.post("/watchlist/serie")
def add_serie_to_watchlist(
        *,
        session: Session = Depends(get_session),
        watchlist_create: WatchlistCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        serie_id = watchlist_create.serie_id
        if not session.query(Serie).filter(Serie.serie_id == serie_id).first():
            raise HTTPException(status_code=404, detail="Serie not found")

        profile_id = watchlist_create.profile_id
        if not session.query(Profile).filter(Profile.profile_id == profile_id).first():
            raise HTTPException(status_code=404, detail="Profile not found")

        watchlist = Watchlist(**watchlist_create.dict())
        session.add(watchlist)
        session.commit()
        return return_created()