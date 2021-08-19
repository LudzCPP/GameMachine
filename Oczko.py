from tkinter import *
from random import *


class Oczko(Tk):
	def __init__(self):
		super().__init__()
		self.title("Oczko")
		self.geometry("500x420")
		self.resizable(False, False)

		self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4]
		self.player_cards = []
		self.player_score = 0
		self.computer_score = randint(12, 21)

		self.game_title = Label(self, text="Oczko", width=31, height=3, bg="grey", font=("Arial", 20))
		self.game_title.grid(row=0, column=0, columnspan=3)

		self.show_current_score = Label(self, text="Obecny wynik: \n\n0", font=("Arial", 15))
		self.show_current_score.grid(row=1, column=0, pady=15)

		self.show_computer_score = Label(self, text="Wynik komputera: \n\n0", font=("Arial", 15))
		self.show_computer_score.grid(row=3, column=0)

		self.show_drawn_card = Label(self, text="Dobrana karta: \n\n", font=("Arial", 15))
		self.show_drawn_card.grid(row=1, column=1)

		self.take_button = Button(self, text="Dobierz kartę!", height=3, width=20, command=self.draw_card)
		self.take_button.grid(row=1, column=2)

		self.surrender_button = Button(self, text="Koniec!", height=3, width=20, command=self.surrender)
		self.surrender_button.grid(row=2, column=2)

		self.restart_button = Button(self, text="Spróbuj ponownie!", height=3, width=20, command=self.restart_game)
		self.restart_button.grid(row=4, column=2)

		self.show_cards = Label(self, text="Moje karty: \n\n", font=("Arial", 15))
		self.show_cards.grid(row=3, column=1)

		self.result = Label(self, text="", font=("Arial", 16))
		self.result.grid(row=3, column=2)

		self.mainloop()

	def end_game(self, won):
		self.take_button["state"] = "disable"
		self.surrender_button["state"] = "disable"

		if won:
			self.result.config(text="WYGRAŁEŚ")
		else:
			self.result.config(text="PRZEGRAŁEŚ")

	def draw_card(self):
		drawn_card = choice(self.cards)
		self.player_score += drawn_card
		self.player_cards.append(drawn_card)

		cards_string = [str(card) for card in self.player_cards]
		cards_list = ", ".join(cards_string)

		self.show_drawn_card.config(text="Dobrana karta: \n\n{}".format(drawn_card))
		self.show_current_score.config(text="Obecny wynik: \n\n{}".format(self.player_score))
		self.show_cards.config(text="Moje karty: \n\n{}".format(cards_list))

		if self.player_score > 21:
			self.end_game(False)
		elif self.player_score == 21:
			self.end_game(True)

	def surrender(self):
		# computer_drawn_card = 0
		# while self.computer_score + computer_drawn_card <= 21:
		# 	self.computer_score += computer_drawn_card
		# 	computer_drawn_card = choice(self.cards)
		self.show_computer_score.config(text="Wynik komputera: \n\n{}".format(self.computer_score))
		if self.player_score > self.computer_score:
			self.end_game(True)
		else:
			self.end_game(False)

	def restart_game(self):
		self.player_cards = []
		self.player_score = 0
		self.computer_score = randint(12, 21)

		self.take_button["state"] = "active"
		self.surrender_button["state"] = "active"

		self.show_drawn_card.config(text="Dobrana karta: \n\n")
		self.show_current_score.config(text="Obecny wynik: \n\n{}".format(self.player_score))
		self.show_cards.config(text="Moje karty: \n\n")
		self.show_computer_score.config(text="Wynik komputera: \n\n")
		self.result.config(text="")