"""
NAME: Jacob Bello
DATE: 7/3/2024
CLASS: CST 205
Images for task 1 and 2 are the same because I displayed my image using bootstrap
for both
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

info = {
  'cars' : ['volkswagen', 'audi', 'bmw', 'porsche'],
  'sports' : ['basketball', 'football', 'baseball']

}

@app.route('/')
def task():
  return render_template('lab2.html', info = info)
