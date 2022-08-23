from sqlalchemy import create_engine
import pandas as pd


##create database connection to existing data
engine=create_engine('sqlite:///heroku_practice/parish_data.db', echo=True)
sqlite_connection = engine.connect()

file = pd.read_excel("heroku_practice/Aledo_vs_Timberview_102521.xlsx")

sqlite_table = "Football"
file.to_sql(sqlite_table, sqlite_connection, if_exists='append', index=False)

full_df = pd.read_sql('SELECT * from Football', sqlite_connection)

class Game_Data():
    def full_data():
        return full_df
    
    def queried_data(qtr):
        queried_df = full_df[full_df.QTR==qtr]
        return queried_df
