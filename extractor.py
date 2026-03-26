from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
from file import save_to_file


def extract_wanted(keyword):

    p = sync_playwright().start()

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(
        f"https://www.wanted.co.kr/search?query={keyword}&search_method=direct&tab=position"
    )

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
        time.sleep(1)

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
        company_name = job.find(
            "span",
            class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__company__ByVLu",
        ).text
        qualification = job.find(
            "span",
            class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__location__4_w0l",
        ).text
        reward = job.find("span", class_="JobCard_reward__oCSIQ").text
        job = {
            "title": title,
            "company_name": company_name,
            "qualification": qualification,
            "reward": reward,
            "link": link,
        }
        jobs_db.append(job)

    return jobs_db


def extract_berlin(keyword):
    p = sync_playwright().start()

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(f"https://berlinstartupjobs.com/skill-areas/{keyword}/")

    page.wait_for_load_state("load")

    for i in range(4):
        page.keyboard.down("End")
        time.sleep(1)

    content = page.content()

    browser.close()
    p.stop()

    print("Browser closed")

    soup = BeautifulSoup(content, "html.parser")

    jobs = soup.find_all("li", class_="bjs-jlid")

    jobs_db = []

    for job in jobs:
        link = job.find("a")["href"]
        title = job.find("h4", class_="bjs-jlid__h").text
        company_name = job.find(
            "a",
            class_="bjs-jlid__b",
        ).text
        description = job.find("div", class_="bjs-jlid__description").text
        job = {
            "title": title,
            "company_name": company_name,
            "description": description,
            "link": link,
        }
        jobs_db.append(job)

    return jobs_db


def extract_web3(keyword):
    p = sync_playwright().start()

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(f"https://web3.career/{keyword}-jobs")

    page.wait_for_load_state("load")

    for i in range(4):
        page.keyboard.down("End")
        time.sleep(1)

    content = page.content()

    browser.close()
    p.stop()

    print("Browser closed")

    soup = BeautifulSoup(content, "html.parser")

    jobs = soup.select("tr.table_row:not(.border-paid-table)")

    jobs_db = []

    for job in jobs:
        link = f"https://web3.career{job.find("a")["href"]}"
        title = job.find("h2", class_="fs-6 fs-md-5 fw-bold my-primary")
        if title:
            title = title.text
        company_name = job.find(
            "h3",
        )
        if company_name:
            company_name = company_name.text
        description = job.find("span")
        if description:
            description = description.text
        job = {
            "title": title,
            "company_name": company_name,
            "description": description,
            "link": link,
        }
        jobs_db.append(job)

    return jobs_db


def extract_weworkremotely(keyword):
    p = sync_playwright().start()

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(
        f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}"
    )

    page.wait_for_load_state("load")

    for i in range(4):
        page.keyboard.down("End")
        time.sleep(1)

    content = page.content()

    browser.close()
    p.stop()

    print("Browser closed")

    soup = BeautifulSoup(content, "html.parser")

    jobs = soup.select("li.new-listing-container:not(.feature--ad)")

    jobs_db = []

    for job in jobs:
        link = f"https://weworkremotely.com/{job.find("a")["href"]}"
        title = job.find("h3", class_="new-listing__header__title")
        if title:
            title = title.text
        company_name = job.find("p", class_="new-listing__company-name")
        if company_name:
            company_name = company_name.text
        description = job.find("p", class_="new-listing__company-headquarters")
        if description:
            description = description.text
        job = {
            "title": title,
            "company_name": company_name,
            "description": description,
            "link": link,
        }
        jobs_db.append(job)

    return jobs_db
