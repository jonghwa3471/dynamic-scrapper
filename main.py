from flask import Flask

app = Flask("Job Scrapper")


@app.route("/")
def home():
    return "Welcome home!!"


app.run()
