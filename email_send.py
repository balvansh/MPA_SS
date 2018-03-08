import smtplib
import getpass

from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def emailform():
    with open("/home/thbr/MPA_SS/email_template.txt",'r',encoding='utf-8') as email:
        email_body=email.read()
    return Template(email_body)
# read the emails from the encrypted DB
emails="balvanshh@gmail.com"
# setup SMTP server details
s=smtplib.SMTP(host="smtp.gmail.com",port=587)
s.starttls()
print('Enter email address:')
address=input()
password=getpass.getpass('Enter password:')
s.login(address,password)
#now send the email to all the authorisers


email_body=emailform() #get template
msg=MIMEMultipart()
message=email_body.substitute(USER="Balvansh") #substitute user
message=message+input('Enter a short description: ')
msg['From']=address
msg['To']=emails
msg['Subject']="AUTHORISATION REQUIRED"

msg.attach(MIMEText(message,'plain'))
try:
    s.send_message(msg)
finally:
    print("Message sent")




