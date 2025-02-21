from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
timer = None
random_word = {}

data = pd.read_csv("./data/french_words.csv")
data_list = data.to_dict(orient="records")


def flip_card(word):
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(word_label, text=word["English"], fill="white")
    canvas.itemconfig(language_label, text="English", fill="white")

def get_unlearned_words():
    try:
        learned_data = pd.read_csv("./data/data_learned.csv")
        learned_words_list = learned_data.to_dict(orient="records")
        unlearned_words = [word for word in data_list if word not in learned_words_list]
        return unlearned_words
    except FileNotFoundError:
        return data_list

def next_card():
    global timer, random_word
    if timer:
        window.after_cancel(timer)
    data_to_learn = get_unlearned_words()
    random_word = random.choice(data_to_learn)
    canvas.itemconfig(word_label, text=random_word["French"], fill="black")
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    timer = window.after(3000, flip_card, random_word)
    print(len(data_to_learn))

def add_word_to_learned(word):
    word_df = pd.DataFrame([word])
    try:
        existing_data = pd.read_csv("./data/data_learned.csv")
    except FileNotFoundError:
        word_df.to_csv("./data/data_learned.csv", index=False)
    else:
        updated_data = pd.concat([existing_data, word_df], ignore_index=True)
        updated_data.to_csv("./data/data_learned.csv", index=False)


def right_button_click():
    add_word_to_learned(random_word)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front_img)

right_button = Button(image=right_img,command=right_button_click, highlightthickness=0)
wrong_button = Button(image=wrong_img, command=next_card, highlightthickness=0)
language_label = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)
right_button.grid(column=1 , row=1)
wrong_button.grid(column=0, row=1)

next_card()


window.mainloop()