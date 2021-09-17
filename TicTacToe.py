import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500


class TicTacToe:
	def __init__(self):
		self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption("Tic Tac Toe")
		self.main()

	def main(self):
		pass