import search
import gmail
KEYWORDS = ["java", "contract"]


def is_match(job):
    title = job.get("title", "").lower()
    return any(k in title for k in KEYWORDS)

def create_email(job):
    return f"""
Dear Hiring Manager,

I am writing to apply for the position: {job.get('title')} at {job.get('company')}.

Please find my resume attached for your consideration.

Thank you for your time.

Regards,
Candidate
"""


def main():

    jobs = search.get_jobs()

    print("\n JOB AUTOMATION SYSTEM STARTED\n")

    for job in jobs:

        print("\n----------------------------")
        print("Checking:", job.get("title"))

        # STEP 1: FILTER
        if not is_match(job):
            print("Not matched")
            continue

        print("MATCH FOUND")
        print("Title:", job.get("title"))
        print("Company:", job.get("company"))

        email = job.get("email")  
        apply_link = job.get("apply_link")

        if email:
            try:
                gmail.send_email(
                    to_email=email,
                    subject=f"Job Application - {job.get('title')}",
                    body=create_email(job),
                    attachment_path="resume.pdf"
                )

                print("Email sent successfully")

            except Exception as e:
                print("Email failed:", e)

        
        else:
            if apply_link:
                with open("applied_jobs.txt", "a", encoding="utf-8") as f:
                    f.write(
                        f"{job.get('title')} | {job.get('company')} | {apply_link}\n"
                    )

                print("No email → Apply link saved")

            else:
                print("No email or apply link found")


if __name__ == "__main__":
    main()