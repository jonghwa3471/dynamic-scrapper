from flask import Flask, render_template

app = Flask("Job Scrapper")


@app.route("/")
def home():
    return render_template("home.html", name="nico")


@app.route("/hello")
def hello():
    return "hello!"


app.run()
