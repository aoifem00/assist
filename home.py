from flask import Flask, render_template
from bs4 import BeautifulSoup
import json

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def otherhome():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/learning_style')
def learning_style():
    return render_template('learning_style.html')

@app.route('/kinesthetic')
def kinesthetic():
    return render_template('kinesthetic.html')

@app.route('/visual')
def visual():
    return render_template('visual.html')

@app.route('/auditory')
def auditory():
    return render_template('auditory.html')
if __name__=='__main__':
    app.run(debug=True)
