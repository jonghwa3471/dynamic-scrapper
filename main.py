from flask import Flask, render_template, request, redirect, send_file
from extractor import (
    extract_wanted,
    extract_berlin,
    extract_web3,
    extract_weworkremotely,
)
from file import save_to_file
from flask_frozen import Freezer

app = Flask("Job Scrapper")
freezer = Freezer(app)

db = {}
PREBUILD_KEYWORDS = ["python", "javascript", "typescript", "rust"]


@app.route("/")
def home():
    return render_template("home.html", name="nico")


@app.route("/search/<keyword>/")
def search(keyword):
    keyword = request.args.get("keyword")
    if keyword == None or keyword == "":
        return redirect("/")
    if keyword in db:
        all_jobs = db[keyword]
    else:
        berlin_jobs = extract_berlin(keyword)
        web3_jobs = extract_web3(keyword)
        weworkremotely_jobs = extract_weworkremotely(keyword)
        all_jobs = [*berlin_jobs, *web3_jobs, *weworkremotely_jobs]
        db[keyword] = all_jobs
    return render_template("search.html", keyword=keyword, jobs=all_jobs)


@freezer.register_generator
def search():
    for keyword in PREBUILD_KEYWORDS:
        yield {"keyword": keyword}


if __name__ == "__main__":
    freezer.freeze()

""" @app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None or keyword == "":
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)


app.run(debug=True) """
