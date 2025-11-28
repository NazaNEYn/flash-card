from tkinter import *
from card_manager import FlashCardManager


BACKGROUND_COLOR = "#B1DDC6"

# ##########################

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

card_front_img = canvas.create_image(403, 263, image=card_front)


card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 35, "italic"))
card_word = canvas.create_text(400, 245, text="Word", font=("Ariel", 45, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)

# ##########################################

manager = FlashCardManager(
    window,
    canvas,
    card_front,
    card_front_img,
    card_back,
    card_title,
    card_word,
)
known_button.config(command=manager.known_word)
unknown_button.config(command=manager.unknown_word)


# ##########################################

window.protocol("WM_DELETE_WINDOW", manager.save_progress)

# ##########################################
window.mainloop()
