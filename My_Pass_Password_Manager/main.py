from importlib.metadata import packages_distributions
from tkinter import *
from tkinter import messagebox
import pyperclip
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate():
    letters_ = [let for let in random.sample(letters, 3)]
    symbols_ = [sym for sym in random.sample(symbols, 3)]
    numbers_ = [num for num in random.sample(numbers, 3)]
    password_list = letters_ + symbols_ + numbers_

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_entry.delete(0, "end")
    password_entry.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website= website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if not password or not website or not email:
        messagebox.showinfo(title="Opaaa", message="Please fill all the fields!")
    else:
        ok = messagebox.askokcancel(title=website, message=f"These are the details to be entered: \nEmail: {email}"
                                                           f"\nPassword: {password}\nIs it ok?")
        if ok:
            with open("./passwords.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file="./logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 10))
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:", font=("Arial", 10))
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Arial", 10))
password_label.grid(column=0, row=3)

generate_button = Button(text="Generate", command=generate, highlightthickness=0)
generate_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", width=36, command=save, highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

email_username_entry = Entry(width=35)
email_username_entry.insert(END, string="kkk123@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="w")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w")

window.mainloop()