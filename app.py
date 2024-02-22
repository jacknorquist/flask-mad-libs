from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

STORIES = {"Silly Story" : silly_story, "Excited Story" : excited_story}

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def choose_story():
    return render_template("stories.html", stories = STORIES)

@app.get('/questions')
def show_story_form():
    """Show madlibs form based on Story instance"""

    prompts = request.args
    return render_template("questions.html", prompts = prompts)


@app.get('/<story>/results')
def show_results():
    """Create a story based on form query parameters"""

    story = silly_story.get_result_text(request.args)
    return render_template("results.html", story = story)

#a=request.args.get("a")