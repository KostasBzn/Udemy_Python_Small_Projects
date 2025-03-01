import smtplib
import datetime as dt
import csv
import random

sender = "example_email_sender@gmail.com"
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
        
# Function to load random template and replace the receivers name
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
        receivers_email = row[1]
        receivers_name = row[0]
        email_content = random_template(receivers_name)
        if int(row[2]) == year and int(row[3]) == month and int(row[4]) == day:
            send_email(receivers_email, email_content)

