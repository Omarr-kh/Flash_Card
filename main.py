import tkinter as tk

# Constants
BACKGROUND_COLOR = "#B1DDC6"

# Window
window = tk.Tk()
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

# Canvas
canvas = tk.Canvas(width=800, height=526,
                   background=BACKGROUND_COLOR, highlightthickness=0)

front_photo = tk.PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=front_photo)

lang_text = canvas.create_text(
    400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(
    400, 263, text="Word", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# Buttons
tick_photo = tk.PhotoImage(file="./images/right.png")
tick_button = tk.Button(image=tick_photo, highlightthickness=0, borderwidth=0)
tick_button.grid(row=1, column=0)

x_photo = tk.PhotoImage(file="./images/wrong.png")
x_button = tk.Button(image=x_photo, highlightthickness=0, borderwidth=0)
x_button.grid(row=1, column=1)

# Main Loop
window.mainloop()
