import csv


def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", mode="w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["포지션", "회사명", "경력", "합격보상", "링크"])

    for job in jobs:
        writer.writerow(job.values())
    file.close()
