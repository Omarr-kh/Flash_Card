import tkinter as tk
import pandas as pd
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"
card = {}

# Words Data
words_data = pd.read_csv("./data/french_words.csv")
words_dict = words_data.to_dict(orient="records")

# Functions


def change_card():
    global card
    card = random.choice(words_dict)
    french_word = card["French"]

    canvas.itemconfig(word_text, text=french_word, fill="black")
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(background, image=front_photo)
    window.after(2500, flip)


def flip():
    english_word = card["English"]
    canvas.itemconfig(word_text, text=english_word, fill="white")
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(background, image=back_photo)


# Window
window = tk.Tk()
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

# Canvas
canvas = tk.Canvas(width=800, height=526,
                   background=BACKGROUND_COLOR, highlightthickness=0)

front_photo = tk.PhotoImage(file="./images/card_front.png")
back_photo = tk.PhotoImage(file="./images/card_back.png")
background = canvas.create_image(400, 263, image=front_photo)

lang_text = canvas.create_text(
    400, 150, text="", font=("Ariel", 30, "italic"))
word_text = canvas.create_text(
    400, 263, text="", font=("Ariel", 50, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# Buttons
tick_photo = tk.PhotoImage(file="./images/right.png")
tick_button = tk.Button(
    image=tick_photo, highlightthickness=0, borderwidth=0, command=change_card)
tick_button.grid(row=1, column=0)

x_photo = tk.PhotoImage(file="./images/wrong.png")
x_button = tk.Button(image=x_photo, highlightthickness=0,
                     borderwidth=0, command=change_card)
x_button.grid(row=1, column=1)

change_card()

# Main Loop
window.mainloop()
