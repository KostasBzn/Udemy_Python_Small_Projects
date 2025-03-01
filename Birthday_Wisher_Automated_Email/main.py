
# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import csv
import random

sender = "example_email_sender.gmail.com"
app_password = "sender_app_password"
subject = "Happy Birthday!"
host = "smtp.gmail.com" # Differs for each email provider

# Function to send the Email
def send_email(receiver, email_content):
    with smtplib.SMTP(host) as connection: 
        connection.starttls()
        connection.login(user= sender, password=app_password)
        connection.sendmail(from_addr=sender, to_addrs=receiver,
                            msg=f"Subject:{subject}\n\n{email_content}")
        
# unction to load random template and replace the receivers name
def random_template(name):
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    random_template = random.choice(letters)
    with open(f"./letter_templates/{random_template}", "r") as template:
        email_content = template.read()
        email_content = email_content.replace("[NAME]", name)
    return email_content


        
# Extract year, month and day from timestamp
timestamp = dt.datetime.now()
year = timestamp.year
month = timestamp.month
day = timestamp.day

# Read the csv file
with open("./birthdays.csv", "r") as file:
    birthday_data = csv.reader(file)
    next(birthday_data)
    for row in birthday_data:
        email = row[1]
        if int(row[2]) == year and int(row[3]) == month and int(row[4]) == day:
            send_email(email, "dd")

