from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
import os
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Load environment variables from .env file
load_dotenv()

# Get the environment variables
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

# Create the connection string using the environment variables
db_connection_string = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

# Create the engine using the connection string
db = create_engine(db_connection_string)

base = declarative_base()

# create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)

#instead of connecting to the database, we will create a session
#create a new instance of the sessionmaker, then point to our engine
Session = sessionmaker(db)

#opens an actual session by calling the Session() function
session = Session()

base.metadata.create_all(db)

# Query 1 - select all records from the "Artist" table
""" artists = session.query(Artist)
for artist in artists:
    print(artist.ArtistId, artist.Name, sep=" | ") """

# Query 2 - select only the "Name" column from the "Artist" table
"""
artists = session.query(Artist)
for artist in artists:
    print(artist.Name) """

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
""" artist = session.query(Artist).filter_by(ArtistId=51).first()
print(artist.ArtistId, artist.Name, sep=" | ") """

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
albums = session.query(Album).filter_by(ArtistId=51)
for album in albums:
    print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
            track.TrackId,
            track.Name,
            track.AlbumId,
            track.MediaTypeId,
            track.GenreId,
            track.Composer,
            track.Milliseconds,
            track.Bytes,
            track.UnitPrice,
            sep=" | "
        )