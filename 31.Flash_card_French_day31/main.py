from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data_dict = {}
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(lang, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_background, image=back_img)
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000,func=flip_card)

back_img= PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
canvas_background = canvas.create_image(400, 263, image=front_img)
lang = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=1,column=1, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, background=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=2)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, background=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
right_button.grid(column=2,row=2)

next_card()

window.mainloop()
