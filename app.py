from flask import Flask, render_template, request, url_for, redirect, flash
import pandas as pd
from functions import Game_Data


app = Flask(__name__)

#connect to database

data=Game_Data


@app.route('/logout')
def index():
    return data.full_data()

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)