from flask import Flask, render_template, request, url_for, redirect, flash
import pandas as pd

from flask_sqlalchemy import SQLAlchemy
import os

from sqlalchemy.sql import func

from sqlalchemy import create_engine, func, Column, Integer, String, Date

from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import user, password, port, db, username, app_password


app = Flask(__name__)

#connect to database


url = f'postgresql://{user}:{password}@localhost:{port}/{db}'
engine = create_engine(url)
app.config['SQLALCHEMY_DATABASE_URI'] = url

db = SQLAlchemy(app)


# UPLOAD_FOLDER = 'static/uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session

#create table model
class Football(db.Model):
    __tablename__ = 'football_data'
    
    id = Column(Integer, primary_key = True)
    qtr = Column(Integer)
    play_no = Column(Integer)
    dn = Column(Integer)
    dist = Column(Integer)
    yard_ln = Column(Integer)
    off_form = Column(String)
    def_front = Column(String)
    stunt = Column(String)
    blitz = Column(String)
    coverage = Column(String)
    field_position = Column(String)
    distance = Column(String)
    date_of_game = Column(Date)
    opponent = Column(String)
    
    
    def __repr__(self):
        return "<Football(qtr='%s', play_no='%s', dn='%s', dist='%s', yard_ln='%s', off_form='%s', def_front='%s', stunt='%s', blitz='%s', field_position='%s', distance='%s', date_of_game='%s', opponent='%s')>" % (self.qtr, self.play_no, self.dn, self.dist, self.yard_ln, self.off_form, self.def_front, self.stunt, self.blitz, self.field_position, self.distance, self.date_of_game, self.opponent)

#Base.metadata.create_all(engine)
# db.create_all()
# db.session.add(Football())
# db.session.commit()

#create marshmallow model for jsonify results
class FootballSchema(Schema):
    id = fields.Int()
    qtr = fields.Int()
    play_no = fields.Int()
    dn = fields.Int()
    dist = fields.Int()
    yard_ln = fields.Int()
    off_form = fields.Str()
    def_front = fields.Str()
    stunt = fields.Str()
    blitz = fields.Str()
    coverage = fields.Str()
    field_position = fields.Str()
    distance = fields.Str()
    date_of_game = fields.Date()
    opponent = fields.Str()

schema = FootballSchema(many=True)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)