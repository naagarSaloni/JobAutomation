# Job Automation System

A Python-based automation project that simplifies job searching and applications using the Adzuna API. It fetches live job listings, filters them using keywords, and automates the application process using Gmail SMTP and apply link tracking.


## Features

- Fetch live job postings using Adzuna API  
- Filter jobs using keywords (e.g., Java, Contract)  
- Auto-send job application emails via Gmail SMTP  
- Attach resume automatically in emails  
- Save apply links when email is not available  
- Smart decision system (email OR link, not both)  
- Tracks applied jobs in local file  


## Tech Stack

- Python  
- Adzuna API  
- Gmail SMTP  
- Requests library  


## Project Structure


JobAutomation/
│
├── main.py
├── search.py
├── gmail.py 
├── config.py
├── resume.pdf 
├── applied_jobs.txt 


##  How It Works

1. Fetch jobs from Adzuna API  
2. Filter jobs using keywords  
3. If email exists → send application email  
4. If email not available → save apply link  
5. Maintain log of all applied jobs  


## Setup Instructions

 1. Clone repository
git clone https://github.com/naagarSaloni/JobAutomation.git
cd JobAutomation

 2. Configure API & Email
Update config.py:
ADZUNA_APP_ID = "your_app_id"
ADZUNA_APP_KEY = "your_app_key"
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"

3. Run project
python main.py

Output Example
Job listings fetched successfully
Emails sent for matched jobs
Apply links saved for fallback cases


This project uses only public job APIs and does not scrape or bypass protected platforms like LinkedIn.

👨‍💻 Author - Saloni Naagar

