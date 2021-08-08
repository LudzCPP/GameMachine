from tkinter import *


class GameMachine(Tk):
	def __init__(self):
		super().__init__()
		self.title("Game Machine by Ludz")

		self.geometry("500x380")
		self.resizable(False, False)
		self.config()

		self.app_title = Label(text="Game Machine by Ludz", width=31, height=3, bg="grey", font=("Arial", 20))
		self.app_title.grid(row=0, column=0, columnspan=2)

		self.game_one = Button(text="Gra 1", width=15, height=3, font=("Arial", 15), command="oczko_game")
		self.game_one.grid(row=1, column=0, pady=20)

		self.game_two = Button(text="Gra 2", width=15, height=3, font=("Arial", 15))
		self.game_two.grid(row=1, column=1, pady=20)

		self.game_three = Button(text="Gra 3", width=15, height=3, font=("Arial", 15))
		self.game_three.grid(row=2, column=0, pady=20)

		self.game_four = Button(text="Gra 4", width=15, height=3, font=("Arial", 15))
		self.game_four.grid(row=2, column=1, pady=20)

	# def oczko_game(self):
	# 	self.game_one

