import logging
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
sh.setFormatter(formatter)
logger.addHandler(sh)

context = ssl._create_unverified_context()

smtp_server = "mail.chubb.com"
from_email = "no_reply_cloud_engg@chubb.com"


def sendmail(to_email,subject,body):

    message = MIMEMultipart("alternative")
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject

    message.attach(MIMEText(body,"html"))

    try:
        server = smtplib.SMTP(smtp_server)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.sendmail(from_email,to_email.split(','),message.as_string())
        logger.info("Mail sent")
    except Exception as e:
        logger.error(e)
