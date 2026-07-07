import requests
import config

def fetch_jobs(keyword):
    url = f"https://api.adzuna.com/v1/api/jobs/{config.COUNTRY}/search/1"

    params = {
        "app_id": config.ADZUNA_APP_ID,
        "app_key": config.ADZUNA_APP_KEY,
        "what": keyword,
        "results_per_page": 10,
        "content-type": "application/json"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("API Error:", response.text)
        return []

    data = response.json()

    jobs = []

    for job in data.get("results", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "location": job.get("location", {}).get("display_name"),
            "apply_link": job.get("redirect_url"),
            "source": "Adzuna API"
        })

    return jobs


def get_jobs():
    keywords = ["java developer", "full stack", ".net developer"]

    all_jobs = []

    for k in keywords:
        jobs = fetch_jobs(k)
        all_jobs.extend(jobs)

    return all_jobs