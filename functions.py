from sqlalchemy import create_engine
import pandas as pd


# ##create database connection to existing data
# engine=create_engine('sqlite:///heroku_practice/parish_data.db', echo=True)
# sqlite_connection = engine.connect()

# file = pd.read_excel("heroku_practice/Aledo_vs_Timberview_102521.xlsx")

# sqlite_table = "football"
# file.to_sql(sqlite_table, sqlite_connection, if_exists='append', index=False)

# full_df = pd.read_sql('SELECT * from Football', sqlite_connection)

# class Game_Data():
#     def full_data():
#         return full_df
    
#     def queried_data(qtr):
#         queried_df = full_df[full_df.QTR==qtr]
#         return queried_df


import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, join, outerjoin, MetaData, Table

# create engine to hawaii.sqlite
connect_string = "sqlite:///heroku_practice/parish_data.db"

# reflect the tables
engine = create_engine(connect_string) 
sqlite_connection = engine.connect()

metadata = MetaData()
metadata.reflect(engine)


# reflect an existing database into a new model
Base = automap_base(metadata=metadata)

# reflect the tables
Base.prepare(engine)

# View all of the classes that automap found
print(Base.classes.keys())

# Save references to each table
Football = Base.classes.Football

# #print(Emission)

# # Create a session (link) from Python to the sqlite DB
session = Session(engine)

# #Filter the data for the year >= 1961
results_football = session.query(Football).filter(Football.QTR == 1)
football_df = pd.read_sql(results_football.statement, session.connection())

session.close()


