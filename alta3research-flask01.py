#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import jsonify
from middleware import search_filter

app = Flask(__name__)

instructions = "Use me to look up data on devil fruits, their users, types, and states, and more...Information can be " \
               "filtered by the following:\n\n "
search_criteria = ["[Character] - returns the names of characters who have eaten devil fruit",
    "[Devil Fruit] - returns the devil fruit names",
    "[Class] - returns the classes of devil fruit",
    "[Subclass] - returns the subclasses of devil fruit",
    "[Awakened] - returns yes or no as to whether the fruit is awakened or has awakening potential",
    "[Status] - returns whether the devil fruit has ever been consumed",
    "[All] - No specific criteria. Returns all data",
    "Combine criteria for better results"]

@app.route("/")
def landing():
    return render_template("landing.html", instructions=instructions, criteria=search_criteria)

@app.route("/search", methods=['POST'])
def info():
    if request.method == 'POST':
        if request.form.get('search_field'):
            criteria = request.form.get('search_field').title()
        else:
            criteria = "All"

    return redirect(url_for("results", searched=criteria))

@app.route('/searched/<searched>')
def results(searched):
    res = search_filter(searched)
    return jsonify(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)


