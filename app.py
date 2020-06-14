from flask import Flask, request, render_template  # imports flask
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

# do this every time, instantiate a new application object! Now a server is made.
app = Flask(__name__)


# part of requirements to add debug, make sure this param is the same as the name above "app"
app.config['SECRET_KEY'] = "djofresh13"
debug = DebugToolbarExtension(app)


@app.route('/form')
def show_form():
    return render_template('home.html')


@app.route('/story')
def get_story():
    place = request.args['place']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    plural_noun = request.args['plural_noun']
    return render_template('story.html', place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)
