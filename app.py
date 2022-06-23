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


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)