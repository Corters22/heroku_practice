from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
import pandas as pd
import functions


app = Flask(__name__)

#connect to database

#data=Game_Data


@app.route('/logout')
def index():
    # data = Game_Data.full_data()
    
    # return render_template('home.html',column_names = data.columns.values, 
    #         row_data = list(data.values.tolist()), zip = zip)
    return render_template('home.html')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)