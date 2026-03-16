from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/search?query=flutter&search_method=direct&tab=position")

""" time.sleep(5)

page.click("button.searchButton_6a6844fa")

time.sleep(5)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

time.sleep(5)

page.keyboard.down("Enter")

time.sleep(5)

page.click("a#search_tab_position")

time.sleep(5) """

page.wait_for_load_state("load")

for i in range(4):
    page.keyboard.down("End")
    time.sleep(5)

content = page.content()

browser.close()
p.stop()

print("Browser closed")

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__zQcZs")

jobs_db = []

for job in jobs:
    link = f"https://www.wanted.co.kr{job.find("a")["href"]}"
    title = job.find("strong", class_="JobCard_title___kfvj").text
    company_name = job.find("span", class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__company__ByVLu").text
    qualification = job.find("span", class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__location__4_w0l").text
    reward = job.find("span", class_="JobCard_reward__oCSIQ").text
    job = {
        "title": title,
        "company_name": company_name,
        "qualification": qualification,
        "reward": reward,
        "link": link
    }
    jobs_db.append(job)

file = open("jobs.csv", "w")
writer = csv.writer(file)
writer.writerow(["Title", "Company", "Qualification", "Reward", "Link"])

for job in jobs_db:
    writer.writerow(job.values())