import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

with open("password.txt") as f:
    password = f.read()
    f.close()

sender_email = "m.python.282@gmail.com"
receiver_email = "dkellyisnow@gmail.com"

message = MIMEMultipart()

message["From"] = sender_email
message['To'] = receiver_email
message['Subject'] = "sending mail using python"
body = 'Hi everyone ! \nThis email is from David'
message.attach(MIMEText(body, 'plain')) 
file = "doc.csv"
attachment = open(file,'rb')

obj = MIMEBase('application','octet-stream')

obj.set_payload((attachment).read())
encoders.encode_base64(obj)
obj.add_header('Content-Disposition',"attachment; filename= "+file)

message.attach(obj)

my_message = message.as_string()
email_session = smtplib.SMTP('smtp.gmail.com',587)
email_session.starttls()
email_session.login(sender_email,password)

email_session.sendmail(sender_email,receiver_email,my_message)
email_session.quit()
print("YOUR MAIL HAS BEEN SENT SUCCESSFULLY")