import random
import pandas as pd


class FlashCardManager:
    FILE = "./data/french_words.csv"
    PROGRESS_FILE = "./data/words_to_learn.csv"

    def __init__(
        self,
        window,
        canvas,
        card_front,
        card_front_img,
        card_back,
        card_title,
        card_word,
    ):
        self.window = window
        self.canvas = canvas
        self.card_front = card_front
        self.card_front_img = card_front_img
        self.card_back = card_back
        self.card_title = card_title
        self.card_word = card_word

        # df = pd.read_csv(FlashCardManager.FILE)
        # self.words_to_learn = df.to_dict(orient="records")

        try:
            df = pd.read_csv(FlashCardManager.PROGRESS_FILE)
            print("Loaded words to learn from progress file.")

        except FileNotFoundError:
            df = pd.read_csv(FlashCardManager.FILE)
            print("Loaded full original word list.")

        self.words_to_learn = df.to_dict(orient="records")

        self.current_word = {}
        self.flip_timer = None
        self.known_words = []

        self.next_card()

    def next_card(self):

        if self.flip_timer is not None:
            self.window.after_cancel(self.flip_timer)

        self.current_word = random.choice(self.words_to_learn)
        self.canvas.itemconfig(self.card_title, text="French")
        self.canvas.itemconfig(self.card_word, text=self.current_word["French"])
        self.canvas.itemconfig(self.card_front_img, image=self.card_front)
        self.flip_timer = self.window.after(3000, self.flip_card)

    def flip_card(self):
        self.canvas.itemconfig(self.card_title, text="English")
        self.canvas.itemconfig(self.card_word, text=self.current_word["English"])
        self.canvas.itemconfig(self.card_front_img, image=self.card_back)

    def known_word(self):
        self.known_words.append(self.current_word)
        print(f"Know words: {len(self.known_words)}")
        self.words_to_learn.remove(self.current_word)
        self.next_card()

    def unknown_word(self):
        if self.flip_timer is not None:
            self.window.after_cancel(self.flip_timer)

        print(f"Words left: {len(self.words_to_learn)}")

        self.next_card()

    def save_progress(self):
        left_over_data = pd.DataFrame(self.words_to_learn)
        left_over_data.to_csv(FlashCardManager.PROGRESS_FILE, index=False)

        self.window.destroy()
