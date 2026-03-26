from flask import Flask, render_template
from extractor import extract_berlin, extract_web3, extract_weworkremotely
from flask_frozen import Freezer

app = Flask("Job Scrapper")
freezer = Freezer(app)

KEYWORDS = ["python", "javascript", "typescript", "rust"]
db = None


def extract_all_jobs():
    all_jobs = []

    for keyword in KEYWORDS:
        berlin_jobs = extract_berlin(keyword)
        web3_jobs = extract_web3(keyword)
        weworkremotely_jobs = extract_weworkremotely(keyword)
        all_jobs.extend(berlin_jobs)
        all_jobs.extend(web3_jobs)
        all_jobs.extend(weworkremotely_jobs)

    return all_jobs


@app.route("/")
def search():
    global db

    if db is None:
        db = extract_all_jobs()

    return render_template("search.html", keyword="All Jobs", jobs=db)


if __name__ == "__main__":
    freezer.freeze()
