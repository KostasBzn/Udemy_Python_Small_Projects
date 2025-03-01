##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt

sender = "example_email_sender.gmail.com"
app_password = "sender_app_password"
subject = "Happy Birthday!"
host = "smtp.gmail.com" # Differs for each email provider

def send_email(receiver, email_content):
    with smtplib.SMTP(host) as connection: 
        connection.starttls()
        connection.login(user= sender, password=app_password)
        connection.sendmail(from_addr=sender, to_addrs=receiver,
                            msg=f"Subject:{subject}\n\n{email_content}")

timestamp = dt.datetime.now()
year = timestamp.year
month = timestamp.month
day = timestamp.day

