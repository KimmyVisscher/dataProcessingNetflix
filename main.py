from typing import List, Optional, Type, ForwardRef
from enum import Enum

import xmltodict
from fastapi import Depends, FastAPI, HTTPException, Query, Header
from fastapi.responses import PlainTextResponse
from fastapi.security import APIKeyHeader, APIKeyQuery
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

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
    serie_classification: List["Classification"] = Relationship(back_populates="classification_serie")
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


class Profile(ProfileBase, table=True):
    profile_id: int = Field(default=None, primary_key=True)

    profile_account: Account = Relationship(back_populates="account_profiles")
    # profile_preference: Preference = Relationship(back_populates="preference_account")


class ProfileCreate(ProfileBase):
    pass


class ProfileRead(ProfileBase):
    account_id: int = Field(default=None, foreign_key="account.account_id")
    profile_id: int
    # preference_id: Preference = Field(default=None, foreign_key=


class PreferenceBase(SQLModel):
    preference_id: int = Field(default=None, primary_key=True)
    username: str


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


def subscription_to_xml_string(subscription):
    xml_string = (
        f"<subscription>\n"
        f"  <description>{subscription.description}</description>\n"
        f"  <subscription_price>{subscription.subscription_price}</subscription_price>\n"
        f"  <quality>{subscription.quality}</quality>\n"
        f"</subscription>"
    )
    return xml_string


def movie_to_xml_string(movie):
    xml_string = (
        f"<movie>\n"
        f"  <title>{movie.title}</title>\n"
        f"  <movie_duration>{movie.movie_duration}</movie_duration>\n"
        f"  <age_restriction>{movie.age_restriction}</age_restriction>\n"
        f"</movie>"
    )
    return xml_string


def subtitle_to_xml_string(subtitle):
    xml_string = (
        f"<subtitle>\n"
        f"  <language>{subtitle.language}</language>\n"
        f"  <subtitle_location>{subtitle.subtitle_location}</subtitle_location>\n"
        f"</subtitle>"
    )
    return xml_string


def series_to_xml_string(serie):
    xml_string = (
        f"<serie>\n"
        f"  <serie_name>{serie.serie_name}</serie_name>\n"
        f"  <age_restriction>{serie.age_restriction}</age_restriction>\n"
        f"</serie>"
    )
    return xml_string


def episode_to_xml_string(episode):
    xml_string = (
        f"<episode>\n"
        f"  <title>{episode.title}</title>\n"
        f"  <episode_duration>{episode.episode_duration}</episode_duration>\n"
        f"</episode>"
    )
    return xml_string


def classification_to_xml_string(classification):
    xml_string = (
        f"<classification>\n"
        f"  <classification>{classification.classification}</classification>\n"
        f"</classification>"
    )
    return xml_string


def genre_to_xml_string(genres):
    xml_string = (
        f"<genre>\n"
        f"  <genre>{genres.genre}</genre>\n"
        f"</genre>"
    )
    return xml_string


def account_to_xml_string(account):
    xml_string = (
        f"<account>\n"
        f"  <email>{account.email}</email>\n"
        f"  <payment_method>{account.payment_method}</payment_method>\n"
        f"  <video_quality>{account.video_quality}</video_quality>\n"
        f"  <username>{account.username}</username>\n"
        f"</account>"
    )
    return xml_string


def profile_to_xml_string(profile):
    xml_string = (
        f"<profile>\n"
        f"  <profile_image>{profile.profile_image}</profile_image>\n"
        f"  <profile_child>{profile.profile_child}</profile_child>\n"
        f"  <language>{profile.language}</language>\n"
        f"</profile>"
    )
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
            xml_content = xmltodict.unparse({"movie": movie.dict()}, full_document=False)
            return PlainTextResponse(content=xml_content, media_type="application/xml")
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
            movies_data = {"movie": [movie.dict() for movie in movies]}
            xml_content = xmltodict.unparse(movies_data, full_document=False)
            return PlainTextResponse(content=xml_content, media_type="application/xml")
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
            movies_data = {"movie": [movie.dict() for movie in movies]}
            xml_content = xmltodict.unparse(movies_data, full_document=False)
            return PlainTextResponse(content=xml_content, media_type="application/xml")
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
            series_data = {"serie": [serie.dict() for serie in series]}
            xml_content = xmltodict.unparse(series_data, full_document=False)
            return PlainTextResponse(content=xml_content, media_type="application/xml")
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
            xml_content = xmltodict.unparse({"serie": serie.dict()}, full_document=False)
            return PlainTextResponse(content=xml_content, media_type="application/xml")
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
            xml_content = xmltodict.unparse({"episode": episode.dict()}, full_document=False)
            return PlainTextResponse(content=xml_content, media_type="application/xml")
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
            episodes_data = {"episode": [episode.dict() for episode in episodes]}
            xml_content = xmltodict.unparse(episodes_data, full_document=False)
            return PlainTextResponse(content=xml_content, media_type="application/xml")
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
            series_data = {"serie": [serie.dict() for serie in series]}
            xml_content = xmltodict.unparse(series_data, full_document=False)
            return PlainTextResponse(content=xml_content, media_type="application/xml")
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
            subtitles_data = {"subtitle": [subtitle.dict() for subtitle in subtitles]}
            xml_content = xmltodict.unparse(subtitles_data, full_document=False)
            return PlainTextResponse(content=xml_content, media_type="application/xml")
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
            subtitles_data = {"subtitle": [subtitle.dict() for subtitle in subtitles]}
            xml_content = xmltodict.unparse(subtitles_data, full_document=False)
            return PlainTextResponse(content=xml_content, media_type="application/xml")
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
            account_data = {"account": [account.dict() for account in accounts]}
            xml_content = xmltodict.unparse(account_data, full_document=False)
            return PlainTextResponse(content=xml_content, media_type="application/xml")
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
            xml_content = xmltodict.unparse({"account": account.dict()}, full_document=False)
            return PlainTextResponse(content=xml_content, media_type="application/xml")
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
            profiles_data = {"profile": [profile.dict() for profile in profiles]}
            xml_content = xmltodict.unparse(profiles_data, full_document=False)
            return PlainTextResponse(content=xml_content, media_type="application/xml")
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
            xml_content = xmltodict.unparse({"profile": profile.dict()}, full_document=False)
            return PlainTextResponse(content=xml_content, media_type="application/xml")
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
            watchlist_data = {"watchlist": [watchlist.dict() for watchlist in watchlists]}
            xml_content = xmltodict.unparse(watchlist_data, full_document=False)
            return PlainTextResponse(content=xml_content, media_type="application/xml")
        else:
            return watchlists
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
def create_movie(*, session: Session = Depends(get_session),
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