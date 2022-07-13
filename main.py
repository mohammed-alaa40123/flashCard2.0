from tkinter import *
import pandas as pd
from random import choice

# read data from csv files using pandas the store it in a dictionary

try:
    data = pd.read_csv("data/words_already_learnt.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")

# picking a random card
current_card = choice(to_learn)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg="#B4DDC6")

# Screen Layout

canvas = Canvas(width=800, height=526, )
canvas.config(bg="#B4DDC6", highlightthickness=0)


card_front_img = PhotoImage(file="D:/Mohamed/Projects/python/flashCard2.0/images/card_front.png")
card_back_img = PhotoImage(file="D:/Mohamed/Projects/python/flashCard2.0/images/card_back.png")
cross_img = PhotoImage(file="images/wrong.png")
check_img = PhotoImage(file="images/right.png")

card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="French", font=("Arial", 48, "italic"))
card_word = canvas.create_text(400, 263, text=current_card["French"], font=("Arial", 60, "bold"))


def got_it_right():
    to_learn.remove(current_card)
    next_card()
    df = pd.DataFrame(to_learn)
    df.to_csv("data/words_already_learnt.csv", index=False)


# changing the content
def next_card():
    global current_card
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f'{current_card["French"]}', fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    # flipping the card automatically after 3 seconds
    window.after(3000, func=flip_card)


# showing the flipped card with the english meaning
def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f'{current_card["English"]}', fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# building the buttons
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
known_button = Button(image=check_img, highlightthickness=0, command=got_it_right)

# Placing the items on the screen
canvas.grid(column=0, row=0, columnspan=2)
unknown_button.grid(column=0, row=1)
known_button.grid(column=1, row=1)


# flipping the card automatically after 3 seconds
window.after(3000, func=flip_card)


window.mainloop()
