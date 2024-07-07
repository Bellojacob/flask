from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = 'csumb-otter'

# Define the form class with song title and artist name
class Playlist(FlaskForm):
    song_title = StringField('Song Title', validators=[DataRequired()])
    artist_name = StringField('Artist Name', validators=[DataRequired()])
    submit = SubmitField('Add Song')

# Initialize an empty playlist
playlist = []

# Function to store song details in the playlist
def store_song(my_song, my_artist):
    playlist.append(dict(
        song=my_song,
        artist=my_artist
    ))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Playlist()
    if form.validate_on_submit():
        store_song(form.song_title.data, form.artist_name.data)
        print(playlist)  # Print playlist to console for debugging
        return redirect('/view_playlist')
    return render_template('index.html', form=form)

@app.route('/view_playlist')
def view_playlist():
    return render_template('vp.html', playlist=playlist)


