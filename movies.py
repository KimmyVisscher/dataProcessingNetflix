from main import *


@app.get("/movies/{movie_id}", response_model=MovieRead)
def read_movie(*, session: Session = Depends(get_session),
               movie_id: int,
               api_key_header: Optional[str] = Depends(api_key_header),
               accept: Optional[str] = Header(None)
               ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        movie = session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

        if accept and "application/xml" in accept:
            return Response(content=movie_to_xml_string([movie]), media_type="application/xml")
        else:
            return movie


@app.get("/movies", response_model=List[MovieRead])
def read_movies(*,
                session: Session = Depends(get_session),
                api_key_header: Optional[str] = Depends(api_key_header),
                accept: Optional[str] = Header(None)
                ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        movies = session.query(Movie).all()
        if not movies:
            raise HTTPException(status_code=404, detail="No movies found")

        if accept and "application/xml" in accept:
            return Response(content=movie_to_xml_string(movies), media_type="application/xml")
        else:
            return movies


@app.get("/movies/genre/{genre}", response_model=List[MovieRead])
def read_movies_by_genre(
        *,
        session: Session = Depends(get_session),
        genre: Genre,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        movies = session.query(Movie).filter(Movie.movie_genre.any(genre=genre.value)).all()
        if not movies:
            raise HTTPException(status_code=404, detail="No movies found")

        if accept and "application/xml" in accept:
            return Response(content=movie_to_xml_string(movies), media_type="application/xml")
        else:
            return movies


@app.get("/movies/{movie_id}/genres", response_model=List[GenresRead])
def read_genre_by_movie(
        *,
        session: Session = Depends(get_session),
        movie_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        genres = session.query(Genres).filter(Genres.movie_id == movie_id).all()
        if not genres:
            raise HTTPException(status_code=404, detail="No genres found")

        if accept and "application/xml" in accept:
            return Response(content=genre_to_xml_string(genres), media_type="application/xml")
        else:
            return genres


@app.post("/movies")
def create_movie(*, session: Session = Depends(get_session),
                 movie_create: MovieCreate,
                 api_key_header: Optional[str] = Depends(api_key_header)
                 ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        movie = Movie(**movie_create.dict())
        session.add(movie)
        session.commit()
        return return_created()


@app.put("/movies/{movie_id}", response_model=MovieRead)
def update_movie(
        *,
        session: Session = Depends(get_session),
        movie_id: int,
        movie_update: MovieCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        movie = session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

        for field, value in movie_update.dict().items():
            setattr(movie, field, value)

        session.commit()
        return movie


@app.delete("/movies/{movie_id}")
def delete_movie(*, session: Session = Depends(get_session),
                 movie_id: int,
                 api_key_header: Optional[str] = Depends(api_key_header)
                 ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        movie = session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

        session.delete(movie)
        session.commit()
        return return_deleted()


@app.get("/movies/{movie_id}/imdb")
def get_imdb_rating(movie_id: int,
                    session: Session = Depends(get_session),
                    api_key_header: Optional[str] = Depends(api_key_header),
                    accept: Optional[str] = Header(None)
                    ):
    if check_apikey_role(session, api_key_header, Role.JUNIOR.value):
        movie = session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

        title = movie.title
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

