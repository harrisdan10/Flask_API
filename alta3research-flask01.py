#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import render_template
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


@app.route("/character", methods=['GET', 'POST'])
def character():
    if request.method == 'POST':
        if request.form.get('search_field'):
            criteria = request.form.get('search_field').title()
            results = search_filter(criteria)
        else:
            results = search_filter("All")
    else:
        results = search_filter("All")

    return jsonify(results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)


