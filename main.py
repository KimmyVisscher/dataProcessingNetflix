from typing import List, Optional, Type
from enum import Enum

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.security import APIKeyHeader, APIKeyQuery
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

from secrets import *


class Genre(Enum):
    ACTION = 1
    SCIFI = 2
    FANTASY = 3
    DRAMA = 4
    HORROR = 5
    THRILLER = 6
    ROMANCE = 7
    COMEDY = 8
    ANIMATION = 9
    REALITY = 10


AgeRestriction = Enum("AgeRestriction", ["ALL_AGES", "6_YEARS", "9_YEARS", "12_YEARS", "16_YEARS"])


class ViewerIndication(Enum):
    SEX = 1
    FEAR = 2
    DISCRIMINATION = 3
    DRUG_ALCOHOL_USAGE = 4
    PROFANITY_USAGE = 5


class Role(Enum):
    JUNIOR = 1
    MEDIOR = 2
    SENIOR = 3

    def get_value(role):
        return role.value


class APIKey(SQLModel, table=True):
    apikey: str = Field(default=None, primary_key=True)
    role: Role


class MovieBase(SQLModel):
    title: str
    movie_duration: int

    #characteristics_id: int = Field(default=None, foreign_key="characteristics.characteristics_id")


class Movie(MovieBase, table=True):
    movie_id: Optional[int] = Field(default=None, primary_key=True)

    subtitles: List["Subtitle"] = Relationship(back_populates="movie")
    #characteristics: 'Type[Characteristics]' = Relationship(back_populates="movie")


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


class CharacteristicsBase(SQLModel):
    pass #todo


class Characteristics(CharacteristicsBase, table=True):
    characteristics_id: Optional[int] = Field(default=None, primary_key=True)

    #movie: Movie = Relationship(back_populates="characteristics")
    # add relationship with episode


class CharacteristicsRead(CharacteristicsBase):
    pass


class CharacteristicsCreate(CharacteristicsBase):
    pass


api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

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
def read_movie(*, session: Session = Depends(get_session), movie_id: int, api_key_header: Optional[str] = Depends(api_key_header)):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        movie = session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        return movie
    else:
        raise HTTPException(status_code=401, detail="No permission")



