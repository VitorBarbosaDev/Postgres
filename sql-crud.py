from sqlalchemy import create_engine, Column, Integer, String
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

# create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    programmer_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

#instead of connecting to the database, we will create a session
#create a new instance of the sessionmaker, then point to our engine
Session = sessionmaker(db)

#opens an actual session by calling the Session() function
session = Session()

base.metadata.create_all(db)


# creating records on our Progammer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

""" session.add(ada_lovelace)
session.add(alan_turing)
session.add(grace_hopper)
session.add(margaret_hamilton)
session.add(bill_gates)
session.add(tim_berners_lee) """

""" programmer = session.query(Programmer).filter_by(programmer_id=7).first()
programmer.first_name = "Vitor"
programmer.last_name = "Barbosa"
programmer.gender = "M"
programmer.nationality = "Irish/Brazilian"
programmer.famous_for = "Punch Party"

session.commit() """

""" #updating multiple records
people = session.query(Programmer)
for person in people:
     if person.gender == "F":
         person.gender = "Female"
     elif person.gender == "M":
         person.gender = "Male"
     else:
        print("Gender not defined")

session.commit() """


""" # deleting a single record
fname = input("Enter a first name: ")
lname = input("Enter a last name: ")
programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# defensive programming
if programmer is not None:
    print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
    confirmation = input("Are you sure you want to delete this record? (y/n) ")
    if confirmation.lower() == "y":
        session.delete(programmer)
        session.commit()
        print("Programmer has been deleted")
    else:
        print("Programmer not deleted")
else:
    print("No records found") """

# delete multiple records
""" programmers = session.query(Programmer).filter(Programmer.programmer_id > 7)
for person in programmers:
    print("Programmer Found: ", person.first_name + " " + person.last_name)
    session.delete(person)
    session.commit()
    print("Programmer has been deleted") """

# delete multiple/all records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()

# Query 1 - select all records from the "Programmer" table
programmers = session.query(Programmer)
for programmer in programmers:
    print(
            programmer.programmer_id,
            programmer.first_name + " " + programmer.last_name,
            programmer.gender,
            programmer.nationality,
            programmer.famous_for,
            sep=" | "
        )