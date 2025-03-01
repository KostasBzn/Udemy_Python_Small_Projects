# Birthday Email Automation Project 🎉

This project automates sending birthday emails to recipients listed in a CSV file. It selects a random email template, personalizes it with the recipient's name, and sends the email on their birthday.

---

## Features ✨

- **Randomized Email Templates:** Choose from multiple email templates for variety.
- **Personalized Emails:** Replace placeholders with the recipient's name.
- **Automated Date Checking:** Sends emails only on the recipient's birthday.
- **SMTP Integration:** Uses Gmail's SMTP server to send emails.

---

## Prerequisites 📋

Before running the project, ensure you have the following:

1. **Python 3.x** installed.
2. A **Gmail account** with an **app password** (enable 2FA and generate an app password).
3. A CSV file (`birthdays.csv`) containing recipient data.
4. Email templates (`letter_1.txt`, `letter_2.txt`, `letter_3.txt`) in a folder named `letter_templates`.

---

## CSV File Format Example📄

The `birthdays.csv` file should have the following format:

- name,email,year,month,day
- Alice Johnson,alice.johnson@email.com,1990,05,14
- Bob Smith,bob.smith@email.com,1985,08,22

---

## Usage 🛠️

1. Clone the repository or download the files.
2. Navigate to the folder containing the files.
3. Run the `main.py` script: `python main.py`
