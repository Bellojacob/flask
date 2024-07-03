"""
https://github.com/Bellojacob/flask
NAME: Jacob Bello
DATE: 7/3/2024
CLASS: CST 205
"""
# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5



# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)
# route decorator binds a function to a URL
@app.route('/')
def hello():
  s1 = '<p>Genevieve M. : afaik</p><br><p>Jacob B. : ASAP</p><br><p>Carson M. : AFK</p>'
  return s1

@app.route('/jacob')
def hello2():
  return render_template('template.html')

