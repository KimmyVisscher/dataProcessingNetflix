from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Movie(Base):
    __tablename__ = "Movie"

    movie_id = Column(Integer, primary_key=True)
    title = Column(String)
    movie_duration = Column(Integer)

    subtitles = relationship('Subtitle', back_populates='movie')


class Subtitle(Base):
    __tablename__ = "Subtitle"

    subtitle_id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("Movie.movie_id"))
    language = Column(String)
    subtitle_location = Column(String)

    movie = relationship('Movie', back_populates='subtitle')



