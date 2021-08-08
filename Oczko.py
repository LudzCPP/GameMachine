from tkinter import *


class Oczko(Tk):
	def __init__(self):
		super().__init__()
		self.title("Oczko")
		self.geometry("500x380")
		self.resizable(False, False)

		self.player_cards = [5]

		self.game_title = Label(self, text="Oczko", width=31, height=3, bg="grey", font=("Arial", 20))
		self.game_title.grid(row=0, column=0, columnspan=3)

		self.current_score = Label(self, text="Obecny wynik: \n\n5", font=("Arial", 15))
		self.current_score.grid(row=1, column=0)

		self.current_score = Label(self, text="Dobrana karta: \n\n5", font=("Arial", 15))
		self.current_score.grid(row=1, column=1)

		self.take_button = Button(self, text="Weż kolejną kartę!", height=3, width=20, command=self.draw_card)
		self.take_button.grid(row=1, column=2)

		self.take_button = Button(self, text="Koniec!", height=3, width=20, command=self.surrender)
		self.take_button.grid(row=2, column=2)

		self.show_cards = Label(self, text="Moje karty: \n{}".format(self.player_cards[0]), font=("Arial", 15))
		self.show_cards.grid(row=3, column=1)

		self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4]

		self.mainloop()

	def draw_card(self):
		pass

	def surrender(self):
		pass