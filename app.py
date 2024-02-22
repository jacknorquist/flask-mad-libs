from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

STORIES = {"Silly Story" : silly_story, "Excited Story" : excited_story}

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def choose_story():
    return render_template("stories.html", stories = STORIES.keys())

@app.get('/questions')
def show_story_form():
    """Show madlibs form based on Story instance"""
    current_story = request.args["Stories"]
    prompts = STORIES.get(request.args["Stories"]).prompts
    return render_template("questions.html", story_name = current_story, prompts = prompts)


@app.get('/<story_name>/results')
def show_results(story_name):
    """Create a story based on form query parameters"""
    story = STORIES.get(story_name)
    text = story.get_result_text(request.args)
    return render_template("results.html", text = text)

#a=request.args.get("a")