from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
# app.config['SECRET_KEY'] = "secret"

# debug = DebugToolbarExtension(app)


@app.route('/')
def show():
    return "Hello World"


@app.route('/home1')
def pick_story():
    return render_template('home1.html')


@app.route('/home')
def questions():
    questions = story.prompts
    return render_template('home.html', questions=questions)


@app.route("/story")
def show_story():
    """Show story result."""

    text = story.generate(request.args)

    return render_template("story.html", text=text)


# @app.route('/story')
# def get_story():
#     place = request.args['place']
#     noun = request.args['noun']
#     verb = request.args['verb']
#     adjective = request.args['adjective']
#     plural_noun = request.args['plural_noun']
#     return render_template('story.html', place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)
