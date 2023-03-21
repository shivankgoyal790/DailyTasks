import smtplib
import getpass
try:
    smtp_obj = smtplib.SMTP("smtp.gmail.com",0)
    smtp_obj.ehlo()
except(KeyError):
    print(KeyError)
smtp_obj.starttls()
email = getpass.getpass("enter email;")
password = getpass.getpass('password please')
smtp_obj.login(email,password)
from_address = email
to_address = email
subject = input("enter subject") 
msg = input("enter mssg")
smtp_obj.sendmail(from_address,to_address,subject+msg)