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


class Quality(Enum):
    SD = 1
    HD = 2
    UHD = 3


class Role(Enum):
    JUNIOR = 1
    MEDIOR = 2
    SENIOR = 3

    def get_value(role):
        return role.value


class APIKey(SQLModel, table=True):
    apikey: str = Field(default=None, primary_key=True)
    role: Role


class SubscriptionBase(SQLModel):
    description: str
    subscription_price: float


class Subscription(SubscriptionBase, table=True):
    subscription_id: Optional[int] = Field(default=None, primary_key=True)

    subscription_accounts: List["Account"] = Relationship(back_populates="account_subscription")


class SubscriptionRead(SubscriptionBase):
    subscription_id: int


class SubscriptionCreate(SubscriptionBase):
    pass


class MovieBase(SQLModel):
    title: str
    movie_duration: int
    age_restriction: AgeRestriction


class Movie(MovieBase, table=True):
    movie_id: Optional[int] = Field(default=None, primary_key=True)

    subtitles: List["Subtitle"] = Relationship(back_populates="movie")
    movie_classification: List["Classification"] = Relationship(back_populates="classification_movie")
    movie_genre: List["Genres"] = Relationship(back_populates="genre_movie")


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
    age_restriction: AgeRestriction


class Serie(SerieBase, table=True):
    serie_id: Optional[int] = Field(default=None, primary_key=True)

    episodes: List["Episode"] = Relationship(back_populates="serie")
    serie_classification: List["Classification"] = Relationship(back_populates="classification_serie")
    serie_genre: List["Genres"] = Relationship(back_populates="genre_serie")


class SerieRead(SerieBase):
    serie_id: int


class SerieCreate(SerieBase):
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


class ClassificationBase(SQLModel):
    classification: str

    serie_id: Optional[int] = Field(default=None, foreign_key="serie.serie_id")
    movie_id: Optional[int] = Field(default=None, foreign_key="movie.movie_id")


class Classification(ClassificationBase, table=True):
    classification_id: Optional[int] = Field(default=None, primary_key=True)

    classification_serie: Serie = Relationship(back_populates="serie_classification")
    classification_movie: Movie = Relationship(back_populates="movie_classification")


class ClassificationRead(ClassificationBase):
    pass


class ClassificationCreate(ClassificationBase):
    pass


class GenresBase(SQLModel):
    genre: str

    serie_id: Optional[int] = Field(default=None, foreign_key="serie.serie_id")
    movie_id: Optional[int] = Field(default=None, foreign_key="movie.movie_id")


class Genres(GenresBase, table=True):
    genre_id: int = Field(default=None, primary_key=True)

    genre_serie: Serie = Relationship(back_populates="serie_genre")
    genre_movie: Movie = Relationship(back_populates="movie_genre")


class GenresRead(GenresBase):
    pass


class GenresCreate(GenresBase):
    pass


class AccountBase(SQLModel):
    email: str
    payment_method: str
    video_quality: Quality

    subscription_id: Optional[int] = Field(default=None, foreign_key="subscription.subscription_id")


class Account(AccountBase, table=True):
    account_id: int = Field(default=None, primary_key=True)

    account_subscription : Subscription = Relationship(back_populates="subscription_accounts")


class AccountRead(AccountBase):
    blocked: int


class AccountCreate(AccountBase):
    password: str


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
def read_movie(*, session: Session = Depends(get_session), movie_id: int,
               api_key_header: Optional[str] = Depends(api_key_header)):
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
        raise HTTPException(status_code=403, detail="No permission")

