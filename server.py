"""Calendar Events."""

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session, 
                   jsonify, Markup, Response
                   )
import json

from flask_debugtoolbar import DebugToolbarExtension



app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined



@app.route("/", methods=["GET", "POST"])
def homepage():
    """Homepage."""

    logout = request.args.get("loggedOut")

    if logout:
        session.clear()

        message = Markup("You have been successfully logged out.")
        flash(message)

    date = datetime.now()
    month_year = date.strftime("%B %Y")

    return render_template("home.html", monthYear=month_year)


@app.route("/about")
def about():
    """Says what Our Calendar is and why it exists."""

    return render_template("about.html")










#generate database

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug


    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=4000, host='0.0.0.0')
