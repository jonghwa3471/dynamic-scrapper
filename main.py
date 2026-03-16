from flask import Flask, render_template, request
from extractor import extract_wanted

app = Flask("Job Scrapper")


@app.route("/")
def home():
    return render_template("home.html", name="nico")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    print(f"keyword:{keyword}")
    wanted_jobs = extract_wanted(keyword)
    print(f"jobs:{wanted_jobs}")
    return render_template("search.html", keyword=keyword, jobs=wanted_jobs)


app.run(debug=True)
