from typing import List, Optional, Type, ForwardRef
from enum import Enum

import xmltodict
import requests
from fastapi import Depends, FastAPI, HTTPException, Query, Header
from fastapi.responses import PlainTextResponse
from fastapi.security import APIKeyHeader, APIKeyQuery
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
import random
import string

from secrets import *


class Genre(Enum):
    ACTION = "ACTION"
    SCIFI = "SCIFI"
    FANTASY = "FANTASY"
    DRAMA = "DRAMA"
    HORROR = "HORROR"
    THRILLER = "THRILLER"
    ROMANCE = "ROMANCE"
    COMEDY = "COMEDY"
    ANIMATION = "ANIMATION"
    REALITY = "REALITY"


class AgeRestriction(Enum):
    ALL_AGES = "ALL_AGES"
    SIX_YEARS = "SIX_YEARS"
    NINE_YEARS = "NINE_YEARS"
    TWELVE_YEARS = "TWELVE_YEARS"
    SIXTEEN_YEARS = "SIXTEEN_YEARS"


class ViewerIndication(Enum):
    SEX = "SEX"
    FEAR = "FEAR"
    DISCRIMINATION = "DISCRIMINATION"
    DRUG_ALCOHOL_USAGE = "DRUG_ALCOHOL_USAGE"
    PROFANITY_USAGE = "PROFANITY_USAGE"
    VIOLENCE = "VIOLENCE"


class Quality(Enum):
    SD = "SD"
    HD = "HD"
    UHD = "UHD"


class Role(Enum):
    UNAUTHORIZED = "UNAUTHORIZED"
    JUNIOR = "JUNIOR"
    MEDIOR = "MEDIOR"
    SENIOR = "SENIOR"

    def get_value(role):
        return role.value


class Language(Enum):
    ENGLISH = "ENGLISH"
    DUTCH = "DUTCH"
    FRENCH = "FRENCH"
    SPANISH = "SPANISH"
    GERMAN = "GERMAN"
    ITALIAN = "ITALIAN"
    JAPANESE = "JAPANESE"
    CHINESE = "CHINESE"
    RUSSIAN = "RUSSIAN"
    PORTUGUESE = "PORTUGUESE"
    ARABIC = "ARABIC"
    KOREAN = "KOREAN"


class APIKey(SQLModel, table=True):
    apikey: str = Field(default=None, primary_key=True)
    role: Role


class APIKeyCreate(SQLModel):
    role: Role


class SubscriptionBase(SQLModel):
    description: str
    subscription_price: float
    quality: Quality


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
    movie_watchlists: List["Watchlist"] = Relationship(back_populates="watchlist_movie")


class MovieRead(MovieBase):
    movie_id: int


class MovieCreate(MovieBase):
    pass


class SubtitleBase(SQLModel):
    language: Language
    subtitle_location: str

    movie_id: Optional[int] = Field(default=None, foreign_key="movie.movie_id")
    episode_id: Optional[int] = Field(default=None, foreign_key="episode.episode_id")


Episode = ForwardRef("Episode")


class Subtitle(SubtitleBase, table=True):
    subtitle_id: Optional[int] = Field(default=None, primary_key=True)

    movie: Optional[Movie] = Relationship(back_populates="subtitles")
    subtitle_episode: Optional[Episode] = Relationship(back_populates="episode_subtitles")


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
    serie_genre: List["Genres"] = Relationship(back_populates="genre_serie")
    serie_watchlists: List["Watchlist"] = Relationship(back_populates="watchlist_serie")


class SerieRead(SerieBase):
    serie_id: int


class SerieCreate(SerieBase):
    pass


class EpisodeBase(SQLModel):
    title: str
    episode_duration: int

    serie_id: int = Field(default=None, foreign_key="serie.serie_id")


class Episode(EpisodeBase, table=True):
    episode_id: Optional[int] = Field(default=None, primary_key=True)

    serie: Serie = Relationship(back_populates="episodes")
    episode_subtitles: List["Subtitle"] = Relationship(back_populates="subtitle_episode")
    episode_classification: List["Classification"] = Relationship(back_populates="classification_episode")


class EpisodeRead(EpisodeBase):
    episode_id: int


class EpisodeCreate(EpisodeBase):
    pass


class ClassificationBase(SQLModel):
    classification: ViewerIndication

    episode_id: Optional[int] = Field(default=None, foreign_key="episode.episode_id")
    movie_id: Optional[int] = Field(default=None, foreign_key="movie.movie_id")


class Classification(ClassificationBase, table=True):
    classification_id: Optional[int] = Field(default=None, primary_key=True)

    classification_episode: Optional[Episode] = Relationship(back_populates="episode_classification")
    classification_movie: Optional[Movie] = Relationship(back_populates="movie_classification")


class ClassificationRead(ClassificationBase):
    pass


class ClassificationCreate(ClassificationBase):
    pass


class GenresBase(SQLModel):
    genre: str

    serie_id: Optional[int] = Field(default=None, foreign_key="serie.serie_id")
    movie_id: Optional[int] = Field(default=None, foreign_key="movie.movie_id")


class Genres(GenresBase, table=True):
    genres_id: int = Field(default=None, primary_key=True)

    genre_serie: Serie = Relationship(back_populates="serie_genre")
    genre_movie: Movie = Relationship(back_populates="movie_genre")


class GenresRead(GenresBase):
    pass


class GenresCreate(GenresBase):
    pass


class AccountBase(SQLModel):
    email: str
    payment_method: str
    username: str

    subscription_id: int = Field(foreign_key="subscription.subscription_id")


class Account(AccountBase, table=True):
    account_id: int = Field(default=None, primary_key=True)

    account_subscription: Subscription = Relationship(back_populates="subscription_accounts")
    account_profiles: List["Profile"] = Relationship(back_populates="profile_account")


class AccountRead(AccountBase):
    # blocked: Optional[int]
    pass


class AccountCreate(AccountBase):
    password: str


class ProfileBase(SQLModel):
    profile_image: str
    profile_child: int
    language: Language

    account_id: int = Field(default=None, foreign_key="account.account_id")


Genrespreference = ForwardRef("Genrespreference")
Indicationpreference = ForwardRef("Indicationpreference")
Agepreference = ForwardRef("Agepreference")


class Profile(ProfileBase, table=True):
    profile_id: int = Field(default=None, primary_key=True)

    profile_account: Account = Relationship(back_populates="account_profiles")
    profile_genrepreference: list["Genrespreference"] = Relationship(back_populates="genrepreference_profile")
    profile_indicationpreference: list["Indicationpreference"] = Relationship(back_populates="indicationpreference_profile")
    profile_agepreference: list["Agepreference"] = Relationship(back_populates="agepreference_profile")


class ProfileCreate(ProfileBase):
    pass


class ProfileRead(ProfileBase):
    account_id: int = Field(default=None, foreign_key="account.account_id")
    profile_id: int


class GenrespreferenceBase(SQLModel):
    profile_id: int = Field(default=None, foreign_key="profile.profile_id")
    genre: Genre


class Genrespreference(GenrespreferenceBase, table=True):
    genrepreference_id: int = Field(default=None, primary_key=True)

    genrepreference_profile: Profile = Relationship(back_populates="profile_genrepreference")


class GenrespreferenceRead(GenrespreferenceBase):
    genrepreference_id: int


class GenrespreferenceCreate(GenrespreferenceBase):
    pass


class IndicationpreferenceBase(SQLModel):
    profile_id: int = Field(default=None, foreign_key="profile.profile_id")
    indication: ViewerIndication


class Indicationpreference(IndicationpreferenceBase, table=True):
    indicationpreference_id: int = Field(default=None, primary_key=True)

    indicationpreference_profile: Profile = Relationship(back_populates="profile_indicationpreference")


class IndicationpreferenceRead(IndicationpreferenceBase):
    indicationpreference_id: int


class IndicationpreferenceCreate(IndicationpreferenceBase):
    pass


class AgepreferenceBase(SQLModel):
    profile_id: int = Field(default=None, foreign_key="profile.profile_id")
    agerestriction: AgeRestriction


class Agepreference(AgepreferenceBase, table=True):
    agepreference_id: int = Field(default=None, primary_key=True)

    agepreference_profile: Profile = Relationship(back_populates="profile_agepreference")


class AgepreferenceRead(AgepreferenceBase):
    agepreference_id: int


class AgepreferenceCreate(AgepreferenceBase):
    pass


class WatchlistBase(SQLModel):
    serie_id: Optional[int] = Field(default=None, foreign_key="serie.serie_id")
    movie_id: Optional[int] = Field(default=None, foreign_key="movie.movie_id")
    profile_id: int = Field(default=None, foreign_key="profile.profile_id")


class Watchlist(WatchlistBase, table=True):
    watchlist_id: int = Field(default=None, primary_key=True)

    watchlist_movie: Movie = Relationship(back_populates="movie_watchlists")
    watchlist_serie: Serie = Relationship(back_populates="serie_watchlists")


class WatchlistRead(WatchlistBase):
    watchlist_id: int


class WatchlistCreate(WatchlistBase):
    pass


api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

connect_args = {}
engine = create_engine(connect_string, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


def subscription_to_xml_string(subscriptions):
    xml_string = "<subscriptions>\n"

    for subscription in subscriptions:
        xml_string += (
            f"  <subscription>\n"
            f"      <description>{subscription.description}</description>\n"
            f"      <subscription_price>{subscription.subscription_price}</subscription_price>\n"
            f"      <quality>{subscription.quality}</quality>\n"
            f"  </subscription>"
        )

    xml_string += "</subscriptions>"
    return xml_string


def movie_to_xml_string(movies):
    xml_string = "<movies>\n"

    for movie in movies:
        xml_string += (
            f"  <movie>\n"
            f"      <title>{movie.title}</title>\n"
            f"      <movie_duration>{movie.movie_duration}</movie_duration>\n"
            f"      <age_restriction>{movie.age_restriction}</age_restriction>\n"
            f"  </movie>"
        )

    xml_string += "</movies>"
    return xml_string


def subtitle_to_xml_string(subtitles):
    xml_string = "<subtitles>\n"

    for subtitle in subtitles:
        xml_string += (
            f"  <subtitle>\n"
            f"      <language>{subtitle.language}</language>\n"
            f"      <subtitle_location>{subtitle.subtitle_location}</subtitle_location>\n"
            f"      <movie_id>{subtitle.movie_id}</movie_id>\n"
            f"      <episode_id>{subtitle.episode_id}</episode_id>\n"
            f"  </subtitle>"
        )

    xml_string += "</subtitles>"
    return xml_string


def series_to_xml_string(series):
    xml_string = "<series>\n"

    for serie in series:
        xml_string += (
            f"  <serie>\n"
            f"      <serie_name>{serie.serie_name}</serie_name>\n"
            f"      <age_restriction>{serie.age_restriction}</age_restriction>\n"
            f"  </serie>"
        )

    xml_string += "</series>"
    return xml_string


def episode_to_xml_string(episodes):
    xml_string = "<episodes>\n"

    for episode in episodes:
        xml_string += (
            f"  <episode>\n"
            f"      <title>{episode.title}</title>\n"
            f"      <episode_duration>{episode.episode_duration}</episode_duration>\n"
            f"      <serie_id>{episode.serie_id}</serie_id>\n"
            f"  </episode>"
        )

    xml_string += "</episodes>"
    return xml_string


def classification_to_xml_string(classifications):
    xml_string = "<classifications>\n"

    for classification in classifications:
        xml_string += (
            f"  <classification>\n"
            f"      <classification>{classification.classification}</classification>\n"
            f"      <serie_id>{classification.serie_id}</serie_id>\n"
            f"      <movie_id>{classification.movie_id}</movie_id>\n"
            f"  </classification>"
        )

    xml_string += "</classifications>"
    return xml_string


def genre_to_xml_string(genres_list):
    xml_string = "<genres>\n"

    for genres in genres_list:
        xml_string += (
            f"  <genre>\n"
            f"      <genre>{genres.genre}</genre>\n"
            f"      <serie_id>{genres.serie_id}</serie_id>\n"
            f"      <movie_id>{genres.movie_id}</movie_id>\n"
            f"  </genre>"
        )

    xml_string += "</genres>"
    return xml_string


def account_to_xml_string(accounts):
    xml_string = "<accounts>\n"

    for account in accounts:
        xml_string += (
            f"  <account>\n"
            f"      <email>{account.email}</email>\n"
            f"      <payment_method>{account.payment_method}</payment_method>\n"
            f"      <username>{account.username}</username>\n"
            f"      <subscription_id>{account.subscription_id}</subscription_id>\n"
            f"  </account>"
        )

    xml_string += "</accounts>"
    return xml_string


def profile_to_xml_string(profiles):
    xml_string = "<profiles>\n"

    for profile in profiles:
        xml_string += (
            f"  <profile>\n"
            f"      <profile_image>{profile.profile_image}</profile_image>\n"
            f"      <profile_child>{profile.profile_child}</profile_child>\n"
            f"      <language>{profile.language}</language>\n"
            f"      <account_id>{profile.account_id}</account_id>\n"
            f"  </profile>"
        )

    xml_string += "</profiles>"
    return xml_string


def watchlist_to_xml_string(watchlists):
    xml_string = "<watchlists>\n"

    for watchlist in watchlists:
        xml_string += (
            f"  <watchlist>\n"
            f"      <serie_id>{watchlist.serie_id}</serie_id>\n"
            f"      <movie_id>{watchlist.movie_id}</movie_id>\n"
            f"      <profile_id>{watchlist.profile_id}</profile_id>\n"
            f" </watchlist>"
        )

    xml_string += "</watchlists>"
    return xml_string


def genrepreferences_to_xml_string(genrepreference):
    xml_string = "<genrepreferences>\n"

    for genrepreference in genrepreference:
        xml_string += (
            f"  <genreprefence>\n"
            f"      <genrepreference_id>{genrepreference.genrepreference_id}</genrepreference_id>\n"
            f"      <genre>{genrepreference.genre}</genre>\n"
            f"      <profile_id>{genrepreference.profile_id}</profile_id>\n"
            f" </genrepreference>"
        )

    xml_string += "</genrepreferences>"
    return xml_string


def indicationpreferences_to_xml_string(indicationpreference):
    xml_string = "<indicationpreferences>\n"

    for indicationpreference in indicationpreference:
        xml_string += (
            f"  <indicationprefence>\n"
            f"      <indicationpreference_id>{indicationpreference.indicationpreference_id}</indicationpreference_id>\n"
            f"      <indication>{indicationpreference.indication}</indication>\n"
            f"      <profile_id>{indicationpreference.profile_id}</profile_id>\n"
            f" </indicationpreference>"
        )

    xml_string += "</indicationpreferences>"
    return xml_string


def agepreferences_to_xml_string(agepreference):
    xml_string = "<agepreferences>\n"

    for agepreference in agepreference:
        xml_string += (
            f"  <agepreference>\n"
            f"      <agepreference_id>{agepreference.agepreference_id}</agepreference_id>\n"
            f"      <agerestriction>{agepreference.agerestriction}</agerestriction>\n"
            f"      <profile_id>{agepreference.profile_id}</profile_id>\n"
            f" </agepreference>"
        )

    xml_string += "</agepreferences>"
    return xml_string


def return_created():
    return Response(status_code=201, content="Created")


def return_deleted():
    return Response(status_code=204, content="Resource deleted succesfully")


app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


def check_role_value(role):
    if role == Role.JUNIOR.value:
        return 1
    elif role == Role.MEDIOR.value:
        return 2
    elif role == Role.SENIOR.value:
        return 3
    elif role == Role.UNAUTHORIZED.value:
        return 0


def check_apikey_role(session, apikey, rolevalue):
    api_key_db = session.get(APIKey, apikey)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")
    elif check_role_value(api_key_db.role.value) >= check_role_value(rolevalue):
        return True
    else:
        raise HTTPException(status_code=403, detail="No permission")


import movies
import series
import account
import watchlist
import preferences
import apikeys
import classification
import subscription