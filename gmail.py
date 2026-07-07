import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import config


def send_email(to_email, subject, body, attachment_path):
    try:
        msg = MIMEMultipart()
        msg['From'] = config.EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # attach resume
        attachment = open(attachment_path, "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            'attachment; filename="resume.pdf"'
        )

        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(config.EMAIL, config.PASSWORD)
        server.send_message(msg)
        server.quit()

        print(f" Email sent to {to_email}")

    except Exception as e:
        print(f" Failed to send email: {e}")