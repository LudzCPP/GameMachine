from tkinter import *


class GameMachine(Tk):
	def __init__(self):
		super().__init__()
		self.title("Game Machine by Ludz")
		self.minsize(width=500, height=500)

		self.app_title = Label(text="Game Machine by Ludz", width=50, height=3, bg="red", font=("Arial", 20))
		self.app_title.grid(row=0, column=0, columnspan=2)

		self.game_one = Button(text="Gra 1", width=20, height=4)
		self.game_one.grid(row=1, column=0)

		self.game_two = Button(text="Gra 2", width=20, height=4)
		self.game_two.grid(row=1, column=1)

		self.game_three = Button(text="Gra 3", width=20, height=4)
		self.game_three.grid(row=2, column=0)

		self.game_four = Button(text="Gra 4", width=20, height=4)
		self.game_four.grid(row=2, column=1)


