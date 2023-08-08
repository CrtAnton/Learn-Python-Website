from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/introduction")
def introduction():
    return render_template("introduction.html")

@views.route("/decision_making")
def decision_making():
    return render_template("decision_making.html")

@views.route("/dictionaries")
def dictionaries():
    return render_template("distionaries.html")

@views.route("/functions")
def functions():
    return render_template("functions.html")

@views.route("/lists")
def lists():
    return render_template("lists.html")

@views.route("/loops")
def loops():
    return render_template("loops.html")

@views.route("/more_projects")
def more_projects():
    return render_template("more_projects.html")

@views.route("/object_oriented_programming")
def object_oriented_programming():
    return render_template("object_oriented_programming.html")

@views.route("/projects")
def projects():
    return render_template("projects.html")

@views.route("/solutions")
def solutions():
    return render_template("solutions.html")

@views.route("/working_with_files")
def working_with_files():
    return render_template("working_with_files.html")