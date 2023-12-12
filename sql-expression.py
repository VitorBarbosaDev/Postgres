from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Float
import os
from dotenv import load_dotenv

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

meta = MetaData(db)

artist_table = Table(
    "Artist",
    meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String),
)

album_table = Table(
    "Album",
    meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("Artist.ArtistId")),
)

track_table = Table(
    "Track",
    meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("Album.AlbumId")),
    Column("MediaTypeId", Integer),
    Column("GenreId", Integer),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float),

)

# making the connection
with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 - select only the "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - select only 'Queen' from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - select only by 'ArtistId' #51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - select all tracks where the composer is 'Queen' from the "Track" table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)


    conn.close()