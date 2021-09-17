from tkinter import *
from Oczko import Oczko
from Shooter import Shooter
from Football import Football
from TicTacToe import TicTacToe


class GameMachine(Tk):
	def __init__(self):
		super().__init__()
		self.title("Game Machine by Ludz")

		self.geometry("500x380")
		self.resizable(False, False)

		self.app_title = Label(text="Game Machine by Ludz", width=31, height=3, bg="grey", font=("Arial", 20))
		self.app_title.grid(row=0, column=0, columnspan=2)

		self.game_one = Button(text="Oczko", width=15, height=3, font=("Arial", 15), command=self.game_one)
		self.game_one.grid(row=1, column=0, pady=20)

		self.game_two = Button(text="Shooter", width=15, height=3, font=("Arial", 15), command=self.game_two)
		self.game_two.grid(row=1, column=1, pady=20)

		self.game_three = Button(text="Football", width=15, height=3, font=("Arial", 15), command=self.game_three)
		self.game_three.grid(row=2, column=0, pady=20)

		self.game_four = Button(text="Tic Tac Toe", width=15, height=3, font=("Arial", 15), command=self.game_four)
		self.game_four.grid(row=2, column=1, pady=20)

		self.mainloop()

	def game_one(self):
		# self.destroy()
		oczko = Oczko()

	def game_two(self):
		shooter = Shooter()

	def game_three(self):
		football = Football()

	def game_four(self):
		tictactoe = TicTacToe()



