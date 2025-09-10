from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#fff"
to_learn = {}
current_card = {}

# ---------------- Data Set up ---------------- #
try:
    data = pandas.read_csv('data/words_to_learn.csv.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/it_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

# print(to_learn)


# ---------------- Functionality Set up ---------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card['Italiano'])
    canvas.itemconfig(card_title, text='Italian', fill='black')
    canvas.itemconfig(card_word, text=current_card['Italiano'], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_cards)


def flip_cards():
    canvas.itemconfig(card_title, text='Español', fill='white')
    canvas.itemconfig(card_word, text=current_card['Español'], fill='white')
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)

    next_card()


# ---------------- Windows Set up ---------------- #
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_cards)


# ---------------- Canvas Set up ---------------- #
canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file='images/card_front.png')
card_background = canvas.create_image(400, 263, image=card_front_img)

card_back_image = PhotoImage(file='images/card_back.png')

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, font=('Calibri', 35, 'bold italic'))

card_word = canvas.create_text(400, 263, font=('Calibri', 50, 'normal'))

# ---------------- Buttons ---------------- #
cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image)
unknown_button.config(highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
know_button = Button(image=check_image)
know_button.config(highlightthickness=0, command=is_known)
know_button.grid(row=1, column=1)

next_card()

window.mainloop()
