from main import *


@app.post("/movies/{movie_id}/classification", response_model=ClassificationRead)
def create_classification_movie(
    *,
    session: Session = Depends(get_session),
    movie_id: int,
    classification_create: ClassificationCreate,
    api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        movie = session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

        classification_data = classification_create.dict()
        classification_data["movie_id"] = movie_id

        classification = Classification(**classification_data)
        session.add(classification)
        session.commit()
        return classification


@app.post("/episodes/{episode_id}/classification", response_model=ClassificationRead)
def create_classification_episode(
    *,
    session: Session = Depends(get_session),
    episode_id: int,
    classification_create: ClassificationCreate,
    api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        episode = session.get(Episode, episode_id)
        if not episode:
            raise HTTPException(status_code=404, detail="Episode not found")

        classification_data = classification_create.dict()
        classification_data["episode_id"] = episode_id

        classification = Classification(**classification_data)
        session.add(classification)
        session.commit()
        return classification


@app.delete("/classifications/{classification_id}")
def delete_classification(*, session: Session = Depends(get_session),
                   classification_id: int,
                   api_key_header: Optional[str] = Depends(api_key_header)
                   ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        classification = session.get(Classification, classification_id)
        if not classification:
            raise HTTPException(status_code=404, detail="Profile not found")

        session.delete(classification)
        session.commit()
        return {"message": "Classification deleted successfully"}


@app.put("/classifications/{classification_id}", response_model=ClassificationRead)
def update_classification(
        *,
        session: Session = Depends(get_session),
        classification_id: int,
        watchlist_update: WatchlistCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        classification = session.get(Classification, classification_id)
        if not classification:
            raise HTTPException(status_code=404, detail="Classification not found")

        for field, value in watchlist_update.dict().items():
            setattr(classification, field, value)

        session.commit()
        return classification