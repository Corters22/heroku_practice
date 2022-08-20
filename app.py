from flask import Flask, render_template, request, url_for, redirect, flash
import pandas as pd


app = Flask(__name__)

#connect to database




@app.route('/')
def index():
    return render_template('base.html')

@app.route('/home')
def home():
    return "This is the home page"

if __name__ == '__main__':
    app.run(debug=True)