from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "daking_negs_developers"

@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", nice to meet you.")
    return render_template("index.html")

