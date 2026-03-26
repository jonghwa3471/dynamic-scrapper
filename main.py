from flask import Flask, render_template, redirect
from extractor import extract_berlin, extract_web3, extract_weworkremotely
from flask_frozen import Freezer

app = Flask("Job Scrapper")
freezer = Freezer(app)

KEYWORDS = ["python", "javascript", "typescript", "rust"]
db = {}


def extract_jobs_by_keyword(keyword):
    berlin_jobs = extract_berlin(keyword)
    web3_jobs = extract_web3(keyword)
    weworkremotely_jobs = extract_weworkremotely(keyword)
    return [*berlin_jobs, *web3_jobs, *weworkremotely_jobs]


@app.route("/")
def home():
    return render_template("home.html", keywords=KEYWORDS)


@app.route("/search/<keyword>/")
def search(keyword):
    keyword = keyword.lower()

    if keyword not in KEYWORDS:
        return redirect("/")

    if keyword not in db:
        db[keyword] = extract_jobs_by_keyword(keyword)

    return render_template("search.html", keyword=keyword, jobs=db[keyword])


@freezer.register_generator
def search():
    for keyword in KEYWORDS:
        yield {"keyword": keyword}


if __name__ == "__main__":
    freezer.freeze()
