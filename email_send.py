import smtplib
import getpass
# read the emails from the encrypted DB
emails=["bryan.robert@btech.christuniversity.in"]
# setup SMTP server details
s=smtplib.SMTP(host="smtp.gmail.com",port=587)
s.starttls()
print('Enter email address:')
address=input()
password=getpass.getpass('Enter password:')
