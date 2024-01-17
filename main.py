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
    JUNIOR = 1
    MEDIOR = 2
    SENIOR = 3

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
    classification: str

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
    pass


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


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/movies/{movie_id}", response_model=MovieRead)
def read_movie(*, session: Session = Depends(get_session),
               movie_id: int,
               api_key_header: Optional[str] = Depends(api_key_header),
               accept: Optional[str] = Header(None)
               ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        movie = session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

        if accept and "application/xml" in accept:
            # xml_content = xmltodict.unparse({"movie": movie.dict()}, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=movie_to_xml_string([movie]), media_type="application/xml")
        else:
            return movie
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/movies", response_model=List[MovieRead])
def read_movies(*,
                session: Session = Depends(get_session),
                api_key_header: Optional[str] = Depends(api_key_header),
                accept: Optional[str] = Header(None)
                ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        movies = session.query(Movie).all()
        if not movies:
            raise HTTPException(status_code=404, detail="No movies found")

        if accept and "application/xml" in accept:
            # movies_data = {"movie": [movie.dict() for movie in movies]}
            # xml_content = xmltodict.unparse(movies_data, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=movie_to_xml_string(movies), media_type="application/xml")
        else:
            return movies
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/movies/genre/{genre}", response_model=List[MovieRead])
def read_movies_by_genre(
        *,
        session: Session = Depends(get_session),
        genre: Genre,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        movies = session.query(Movie).filter(Movie.movie_genre.any(genre=genre.value)).all()
        if not movies:
            raise HTTPException(status_code=404, detail="No movies found")

        if accept and "application/xml" in accept:
            # movies_data = {"movie": [movie.dict() for movie in movies]}
            # xml_content = xmltodict.unparse(movies_data, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=movie_to_xml_string(movies), media_type="application/xml")
        else:
            return movies
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/series", response_model=List[SerieRead])
def read_series(*, session: Session = Depends(get_session),
                api_key_header: Optional[str] = Depends(api_key_header),
                accept: Optional[str] = Header(None)
                ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        series = session.query(Serie).all()
        if not series:
            raise HTTPException(status_code=404, detail="No series found")

        if accept and "application/xml" in accept:
            # series_data = {"serie": [serie.dict() for serie in series]}
            # xml_content = xmltodict.unparse(series_data, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=series_to_xml_string(series), media_type="application/xml")
        else:
            return series
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/series/{serie_id}", response_model=SerieRead)
def read_series(*, session: Session = Depends(get_session),
                serie_id: int,
                api_key_header: Optional[str] = Depends(api_key_header),
                accept: Optional[str] = Header(None)
                ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        serie = session.get(Serie, serie_id)
        if not serie:
            raise HTTPException(status_code=404, detail="No series found")

        if accept and "application/xml" in accept:
            # xml_content = xmltodict.unparse({"serie": serie.dict()}, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=series_to_xml_string([serie]), media_type="application/xml")
        else:
            return serie
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/episodes/{episode_id}", response_model=EpisodeRead)
def read_episode(*, session: Session = Depends(get_session),
                episode_id: int,
                api_key_header: Optional[str] = Depends(api_key_header),
                accept: Optional[str] = Header(None)
                ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        episode = session.get(Episode, episode_id)
        if not episode:
            raise HTTPException(status_code=404, detail="Episode not found")

        if accept and "application/xml" in accept:
            # xml_content = xmltodict.unparse({"episode": episode.dict()}, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=episode_to_xml_string([episode]), media_type="application/xml")
        else:
            return episode
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/series/{serie_id}/episodes", response_model=List[EpisodeRead])
def read_episodes_by_serie(
    *,
    session: Session = Depends(get_session),
    serie_id: int,
    api_key_header: Optional[str] = Depends(api_key_header),
    accept: Optional[str] = Header(None),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        serie = session.get(Serie, serie_id)
        if not serie:
            raise HTTPException(status_code=404, detail="Serie not found")

        episodes = session.query(Episode).filter(Episode.serie_id == serie_id).all()
        if not episodes:
            raise HTTPException(status_code=404, detail="No episodes found for the serie")

        if accept and "application/xml" in accept:
            # episodes_data = {"episode": [episode.dict() for episode in episodes]}
            # xml_content = xmltodict.unparse(episodes_data, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=episode_to_xml_string(episodes), media_type="application/xml")
        else:
            return episodes
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/series/genre/{genre}", response_model=List[SerieRead])
def read_series_by_genre(
        *,
        session: Session = Depends(get_session),
        genre: Genre,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        series = session.query(Serie).filter(Serie.serie_genre.any(genre=genre.value)).all()
        if not series:
            raise HTTPException(status_code=404, detail="No series found")

        if accept and "application/xml" in accept:
            # series_data = {"serie": [serie.dict() for serie in series]}
            # xml_content = xmltodict.unparse(series_data, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=series_to_xml_string(series), media_type="application/xml")
        else:
            return series
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/movies/{movie_id}/subtitles", response_model=List[SubtitleRead])
def read_subtitles_by_movie(
        *,
        session: Session = Depends(get_session),
        movie_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
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
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/episodes/{episode_id}/subtitles", response_model=List[SubtitleRead])
def read_subtitles_by_episode(
        *,
        session: Session = Depends(get_session),
        episode_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
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
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/accounts", response_model=List[AccountRead])
def read_accounts(*,
                session: Session = Depends(get_session),
                api_key_header: Optional[str] = Depends(api_key_header),
                accept: Optional[str] = Header(None)
                ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        accounts = session.query(Account).all()
        if not accounts:
            raise HTTPException(status_code=404, detail="No accounts found")

        if accept and "application/xml" in accept:
            # account_data = {"account": [account.dict() for account in accounts]}
            # xml_content = xmltodict.unparse(account_data, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=account_to_xml_string(accounts), media_type="application/xml")
        else:
            return accounts
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/accounts/{account_id}", response_model=AccountRead)
def read_account(*, session: Session = Depends(get_session),
               account_id: int,
               api_key_header: Optional[str] = Depends(api_key_header),
               accept: Optional[str] = Header(None)
               ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        account = session.get(Account, account_id)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")

        if accept and "application/xml" in accept:
            # xml_content = xmltodict.unparse({"account": account.dict()}, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=account_to_xml_string([account]), media_type="application/xml")
        else:
            return account
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/accounts/{account_id}/profiles", response_model=List[ProfileRead])
def read_profiles_by_account(
        *,
        session: Session = Depends(get_session),
        account_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        profiles = session.query(Profile).filter(Profile.account_id == account_id).all()
        if not profiles:
            raise HTTPException(status_code=404, detail="No profiles found")

        if accept and "application/xml" in accept:
            # profiles_data = {"profile": [profile.dict() for profile in profiles]}
            # xml_content = xmltodict.unparse(profiles_data, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=profile_to_xml_string(profiles), media_type="application/xml")
        else:
            return profiles
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/profiles/{profile_id}", response_model=ProfileRead)
def read_profile_by_id(*, session: Session = Depends(get_session),
               profile_id: int,
               api_key_header: Optional[str] = Depends(api_key_header),
               accept: Optional[str] = Header(None)
               ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        profile = session.get(Profile, profile_id)
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")

        if accept and "application/xml" in accept:
            # xml_content = xmltodict.unparse({"profile": profile.dict()}, full_document=False)
            # return PlainTextResponse(content=xml_content, media_type="application/xml")
            return Response(content=profile_to_xml_string([profile]), media_type="application/xml")
        else:
            return profile
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/profiles/{profile_id}/watchlist", response_model=List[WatchlistRead])
def read_watchlist_by_profile(
        *,
        session: Session = Depends(get_session),
        profile_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
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
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/profiles/{profile_id}/genrepreference", response_model=List[GenrespreferenceRead])
def read_genrepreference_by_profile(
        *,
        session: Session = Depends(get_session),
        profile_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        genrepreferences = session.query(Genrespreference).filter(Genrespreference.profile_id == profile_id).all()
        if not genrepreferences:
            raise HTTPException(status_code=404, detail="No genrepreferences found")

        if accept and "application/xml" in accept:
            return Response(content=genrepreferences_to_xml_string(genrepreferences), media_type="application/xml")
        else:
            return genrepreferences
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/genrepreferences/{genrepreference_id}", response_model=GenrespreferenceRead)
def read_genrepreference_by_id(
        *,
        session: Session = Depends(get_session),
        genrepreference_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        genrepreference = session.get(Genrespreference, genrepreference_id)
        if not genrepreference:
            raise HTTPException(status_code=404, detail="No genrepreferences found")

        if accept and "application/xml" in accept:
            return Response(content=genrepreferences_to_xml_string(([genrepreference])), media_type="application/xml")
        else:
            return genrepreference
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/profiles/{profile_id}/indicationpreferences", response_model=List[IndicationpreferenceRead])
def read_indicationpreference_by_profile(
        *,
        session: Session = Depends(get_session),
        profile_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        indicationpreferences = session.query(Indicationpreference).filter(Indicationpreference.profile_id == profile_id).all()
        if not indicationpreferences:
            raise HTTPException(status_code=404, detail="No indicationpreferences found")

        if accept and "application/xml" in accept:
            return Response(content=indicationpreferences_to_xml_string(indicationpreferences), media_type="application/xml")
        else:
            return indicationpreferences
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/indicationpreferences/{indicationpreference_id}", response_model=IndicationpreferenceRead)
def read_indicationpreference_by_id(
        *,
        session: Session = Depends(get_session),
        indicationpreference_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        indicationpreference = session.get(Indicationpreference, indicationpreference_id)
        if not indicationpreference:
            raise HTTPException(status_code=404, detail="No indicationpreferences found")

        if accept and "application/xml" in accept:
            return Response(content=indicationpreferences_to_xml_string(([indicationpreference])), media_type="application/xml")
        else:
            return indicationpreference
    else:
        raise HTTPException(status_code=403, detail="No permission")




@app.get("/profiles/{profile_id}/agepreferences", response_model=List[AgepreferenceRead])
def read_agepreferences_by_profile(
        *,
        session: Session = Depends(get_session),
        profile_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        agepreferences = session.query(Agepreference).filter(Agepreference.profile_id == profile_id).all()
        if not agepreferences:
            raise HTTPException(status_code=404, detail="No agepreferences found")

        if accept and "application/xml" in accept:
            return Response(content=agepreferences_to_xml_string(agepreferences), media_type="application/xml")
        else:
            return agepreferences
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/agepreferences/{agepreference_id}", response_model=AgepreferenceRead)
def read_agepreference_by_id(
        *,
        session: Session = Depends(get_session),
        agepreference_id: int,
        api_key_header: str = Depends(api_key_header),
        accept: str = Header(None),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        agepreference = session.get(Agepreference, agepreference_id)
        if not agepreference:
            raise HTTPException(status_code=404, detail="No agepreferences found")

        if accept and "application/xml" in accept:
            return Response(content=agepreferences_to_xml_string(([agepreference])), media_type="application/xml")
        else:
            return agepreference
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.post("/movies", response_model=MovieRead)
def create_movie(*, session: Session = Depends(get_session),
                 movie_create: MovieCreate,
                 api_key_header: Optional[str] = Depends(api_key_header)
                 ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        movie = Movie(**movie_create.dict())
        session.add(movie)
        session.commit()
        return movie
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.post("/series", response_model=SerieRead)
def create_serie(*, session: Session = Depends(get_session),
                 serie_create: SerieCreate,
                 api_key_header: Optional[str] = Depends(api_key_header)
                 ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        serie = Serie(**serie_create.dict())
        session.add(serie)
        session.commit()
        return serie
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.post("/episodes", response_model=EpisodeRead)
def create_episode(
        *,
        session: Session = Depends(get_session),
        episode_create: EpisodeCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level < Role.JUNIOR.value:
        raise HTTPException(status_code=403, detail="No permission")

    serie_id = episode_create.serie_id
    if not session.query(Serie).filter(Serie.serie_id == serie_id).first():
        raise HTTPException(status_code=404, detail="Serie not found")

    episode = Episode(**episode_create.dict())
    session.add(episode)
    session.commit()
    return episode


@app.post("/episodes/{episode_id}/subtitles", response_model=SubtitleRead)
def create_subtitle_for_episode(
    *,
    session: Session = Depends(get_session),
    episode_id: int,
    subtitle_create: SubtitleCreate,
    api_key_header: Optional[str] = Depends(api_key_header),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level < Role.JUNIOR.value:
        raise HTTPException(status_code=403, detail="No permission")

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
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level < Role.JUNIOR.value:
        raise HTTPException(status_code=403, detail="No permission")

    movie = session.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    subtitle_data = subtitle_create.dict()
    subtitle_data["movie_id"] = movie_id

    subtitle = Subtitle(**subtitle_data)
    session.add(subtitle)
    session.commit()
    return subtitle


@app.post("/accounts", response_model=AccountRead)
def create_account(*, session: Session = Depends(get_session),
                 account_create: AccountCreate,
                 api_key_header: Optional[str] = Depends(api_key_header)
                 ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        account = Account(**account_create.dict())
        session.add(account)
        session.commit()
        return account
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.post("/profiles", response_model=ProfileRead)
def create_profile(
        *,
        session: Session = Depends(get_session),
        profile_create: ProfileCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level < Role.JUNIOR.value:
        raise HTTPException(status_code=403, detail="No permission")

    account_id = profile_create.account_id
    if not session.query(Account).filter(Account.account_id == account_id).first():
        raise HTTPException(status_code=404, detail="Account not found")

    profile = Profile(**profile_create.dict())
    session.add(profile)
    session.commit()
    return profile


@app.put("/movies/{movie_id}", response_model=MovieRead)
def update_movie(
        *,
        session: Session = Depends(get_session),
        movie_id: int,
        movie_update: MovieCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        movie = session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

        for field, value in movie_update.dict().items():
            setattr(movie, field, value)

        session.commit()
        return movie
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.put("/series/{serie_id}", response_model=SerieRead)
def update_serie(
        *,
        session: Session = Depends(get_session),
        serie_id: int,
        serie_update: SerieCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        serie = session.get(Serie, serie_id)
        if not serie:
            raise HTTPException(status_code=404, detail="Serie not found")

        for field, value in serie_update.dict().items():
            setattr(serie, field, value)

        session.commit()
        return serie
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.put("/episodes/{episode_id}", response_model=EpisodeRead)
def update_episode(
        *,
        session: Session = Depends(get_session),
        episode_id: int,
        episode_update: EpisodeCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        episode = session.get(Episode, episode_id)
        if not episode:
            raise HTTPException(status_code=404, detail="Episode not found")

        for field, value in episode_update.dict().items():
            setattr(episode, field, value)

        session.commit()
        return episode
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.put("/subtitles/{subtitle_id}", response_model=SubtitleRead)
def update_subtitle(
        *,
        session: Session = Depends(get_session),
        subtitle_id: int,
        subtitle_update: SubtitleCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        subtitle = session.get(Subtitle, subtitle_id)
        if not subtitle:
            raise HTTPException(status_code=404, detail="Subtitle not found")

        for field, value in subtitle_update.dict().items():
            setattr(subtitle, field, value)

        session.commit()
        return subtitle
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.put("/accounts/{account_id}", response_model=AccountRead)
def update_account(
        *,
        session: Session = Depends(get_session),
        account_id: int,
        account_update: AccountCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        account = session.get(Account, account_id)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")

        for field, value in account_update.dict().items():
            setattr(account, field, value)

        session.commit()
        return account
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.put("/profiles/{profile_id}", response_model=ProfileRead)
def update_profile(
        *,
        session: Session = Depends(get_session),
        profile_id: int,
        profile_update: ProfileCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        profile = session.get(Profile, profile_id)
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")

        for field, value in profile_update.dict().items():
            setattr(profile, field, value)

        session.commit()
        return profile
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.delete("/movies/{movie_id}")
def delete_movie(*, session: Session = Depends(get_session),
                 movie_id: int,
                 api_key_header: Optional[str] = Depends(api_key_header)
                 ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        movie = session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

        session.delete(movie)
        session.commit()
        return {"message": "Movie deleted successfully"}
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.delete("/series/{serie_id}")
def delete_series(*, session: Session = Depends(get_session),
                  serie_id: int,
                  api_key_header: Optional[str] = Depends(api_key_header)
                  ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        serie = session.get(Serie, serie_id)
        if not serie:
            raise HTTPException(status_code=404, detail="Series not found")

        session.delete(serie)
        session.commit()
        return {"message": "Series deleted successfully"}
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.delete("/episodes/{episode_id}")
def delete_episode(*, session: Session = Depends(get_session),
                   episode_id: int,
                   api_key_header: Optional[str] = Depends(api_key_header)
                   ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        episode = session.get(Episode, episode_id)
        if not episode:
            raise HTTPException(status_code=404, detail="Episode not found")

        session.delete(episode)
        session.commit()
        return {"message": "Episode deleted successfully"}
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.delete("/subtitles/{subtitle_id}")
def delete_subtitle(*, session: Session = Depends(get_session),
                    subtitle_id: int,
                    api_key_header: Optional[str] = Depends(api_key_header)
                    ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        subtitle = session.get(Subtitle, subtitle_id)
        if not subtitle:
            raise HTTPException(status_code=404, detail="Subtitle not found")

        session.delete(subtitle)
        session.commit()
        return {"message": "Subtitle deleted successfully"}
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.delete("/accounts/{account_id}")
def delete_account(*, session: Session = Depends(get_session),
                   account_id: int,
                   api_key_header: Optional[str] = Depends(api_key_header)
                   ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        account = session.get(Account, account_id)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")

        session.delete(account)
        session.commit()
        return {"message": "Account deleted successfully"}
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.delete("/profiles/{profile_id}")
def delete_profile(*, session: Session = Depends(get_session),
                   profile_id: int,
                   api_key_header: Optional[str] = Depends(api_key_header)
                   ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
        profile = session.get(Profile, profile_id)
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")

        session.delete(profile)
        session.commit()
        return {"message": "Profile deleted successfully"}
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/movies/{movie_id}/imdb")
def get_imdb_rating(movie_id: int,
                    session: Session = Depends(get_session),
                    api_key_header: Optional[str] = Depends(api_key_header),
                    accept: Optional[str] = Header(None)
                    ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
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
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/series/{serie_id}/imdb")
def get_imdb_rating_by_serie(serie_id: int,
                    session: Session = Depends(get_session),
                    api_key_header: Optional[str] = Depends(api_key_header),
                    accept: Optional[str] = Header(None)
                    ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.JUNIOR.value:
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
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.post("/apikeys/")
def create_api_key(*, session: Session = Depends(get_session),
                   role: str,
                   api_key_header: Optional[str] = Depends(api_key_header)
                   ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.SENIOR.value:
        if role != "JUNIOR" and role != "MEDIOR" and role != "SENIOR":
            raise HTTPException(status_code=400, detail="Invalid role")


        key_length = 15
        letters = string.ascii_letters

        while True:
            api_key = ''.join(random.choice(letters) for _ in range(key_length))
            existing_api_key = session.get(APIKey, api_key)
            if not existing_api_key:
                break

        apikey_model = APIKey(apikey=api_key, role=role)
        session.add(apikey_model)
        session.commit()

        return {"api_key": api_key}
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.delete("/apikeys/{apikey}", response_model=dict)
def delete_api_key(apikey: str,
                   session: Session = Depends(get_session),
                   api_key_header: Optional[str] = Depends(api_key_header)
                   ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.SENIOR.value:
        delete_api_key = session.query(APIKey).filter(APIKey.apikey == apikey).first()
        if not delete_api_key:
            raise HTTPException(status_code=404, detail="API key not found")

        session.delete(delete_api_key)
        session.commit()

        return {"message": "API key deleted successfully"}
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.get("/apikey/{apikey}", response_model=APIKey)
def read_apikey(*, session: Session = Depends(get_session),
                apikey: str,
                api_key_header: Optional[str] = Depends(api_key_header),
                accept: Optional[str] = Header(None)
                ):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level >= Role.SENIOR.value:
        apikey = session.get(APIKey, apikey)
        if not apikey:
            raise HTTPException(status_code=404, detail="APIKey not found")

        if accept and "application/xml" in accept:
            xml_content = xmltodict.unparse({"apikey": apikey.dict()}, full_document=False)
            return PlainTextResponse(content=xml_content, media_type="application/xml")
        else:
            return apikey
    else:
        raise HTTPException(status_code=403, detail="No permission")


@app.post("/watchlist/serie", response_model=WatchlistRead)
def add_serie_to_watchlist(
        *,
        session: Session = Depends(get_session),
        watchlist_create: WatchlistCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level < Role.JUNIOR.value:
        raise HTTPException(status_code=403, detail="No permission")

    serie_id = watchlist_create.serie_id
    if not session.query(Serie).filter(Serie.serie_id == serie_id).first():
        raise HTTPException(status_code=404, detail="Serie not found")

    profile_id = watchlist_create.profile_id
    if not session.query(Profile).filter(Profile.profile_id == profile_id).first():
        raise HTTPException(status_code=404, detail="Profile not found")

    watchlist = Watchlist(**watchlist_create.dict())
    session.add(watchlist)
    session.commit()
    return watchlist


@app.post("/watchlist/movie", response_model=WatchlistRead)
def add_movie_to_watchlist(
        *,
        session: Session = Depends(get_session),
        watchlist_create: WatchlistCreate,
        api_key_header: Optional[str] = Depends(api_key_header),
):
    api_key = api_key_header
    api_key_db = session.get(APIKey, api_key)
    if not api_key_db:
        raise HTTPException(status_code=401, detail="Invalid API key")

    access_level = api_key_db.role.value
    if access_level < Role.JUNIOR.value:
        raise HTTPException(status_code=403, detail="No permission")

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
