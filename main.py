from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

from secrets import *


class MovieBase(SQLModel):
    title: str
    movie_duration: int


class Movie(MovieBase, table=True):
    movie_id: Optional[int] = Field(default=None, primary_key=True)

    subtitles: List["Subtitle"] = Relationship(back_populates="movie")


class MovieRead(MovieBase):
    movie_id: int


class MovieCreate(MovieBase):
    pass


class SubtitleBase(SQLModel):
    language: str
    subtitle_location: str

    movie_id: Optional[int] = Field(default=None, foreign_key="movie.movie_id")


class Subtitle(SubtitleBase, table=True):
    subtitle_id: Optional[int] = Field(default=None, primary_key=True)

    movie: Optional[Movie] = Relationship(back_populates="subtitles")


class SubtitleRead(SubtitleBase):
    subtitle_id: int


class SubtitleCreate(SubtitleBase):
    pass


class SerieBase(SQLModel):
    serie_name: str


class Serie(SerieBase, table=True):
    serie_id: Optional[int] = Field(default=None, primary_key=True)

    episodes: List["Episode"] = Relationship(back_populates="serie")


class SerieRead(SubtitleBase):
    serie_id: int


class SerieCreate(SubtitleBase):
    pass


class EpisodeBase(SQLModel):
    title: str
    episode_duration: int

    characteristics_id: Optional[int]
    serie_id: int = Field(default=None, foreign_key="serie.serie_id")


class Episode(EpisodeBase, table=True):
    episode_id: Optional[int] = Field(default=None, primary_key=True)

    serie: Serie = Relationship(back_populates="episodes")


class EpisodeRead(EpisodeBase):
    episode_id: int


class EpisodeCreate(EpisodeBase):
    pass


connect_args = {}
engine = create_engine(connect_string, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/movies/{movie_id}", response_model=MovieRead)
def read_movie(*, session: Session = Depends(get_session), movie_id: int):
    movie = session.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie



