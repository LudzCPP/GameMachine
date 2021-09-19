import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
BORDER_WIDTH = 10
BORDER = [
	pygame.Rect(WINDOW_WIDTH / 3 - BORDER_WIDTH / 2, 0, BORDER_WIDTH, WINDOW_HEIGHT),
	pygame.Rect(2 * (WINDOW_WIDTH / 3) - BORDER_WIDTH / 2, 0, BORDER_WIDTH, WINDOW_HEIGHT),
	pygame.Rect(0, WINDOW_HEIGHT / 3 - BORDER_WIDTH / 2, WINDOW_WIDTH, BORDER_WIDTH),
	pygame.Rect(0, 2 * (WINDOW_HEIGHT / 3 - BORDER_WIDTH / 2), WINDOW_WIDTH, BORDER_WIDTH)
]

SIGNS = {
	True: 'X',
	False: 'O'
}

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60


class TicTacToe:
	def __init__(self):
		self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.current_sign = True
		self.board = [
			['-', '-', '-'],
			['-', '-', '-'],
			['-', '-', '-']
		]
		pygame.display.set_caption("Tic Tac Toe")
		self.main()

	def main(self):
		clock = pygame.time.Clock()

		run = True
		while run:
			clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					pygame.display.quit()
				if event.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()
					self.click_handle(pos, self.current_sign)

			self.draw_window()

	def draw_window(self):
		self.window.fill(BLACK)
		for rect in BORDER:
			pygame.draw.rect(self.window, WHITE, rect)

		self.draw_shapes()

		pygame.display.update()

	def click_handle(self, pos, current_sign):
		col = int(pos[0] // (WINDOW_WIDTH / 3 - BORDER_WIDTH / 2))
		row = int(pos[1] // (WINDOW_HEIGHT / 3 - BORDER_WIDTH / 2))

		if self.board[row][col] == '-':
			self.board[row][col] = SIGNS[current_sign]
			self.current_sign = not current_sign

		print(BORDER[0].x)

		for row in self.board:
			print(row)

	def draw_shapes(self):
		for row in range(3):
			for col in range(3):
				if self.board[row][col] == 'O':
					pygame.draw.circle(
						self.window,
						WHITE,
						(col * 200 + 100, row * 200 + 100),
						50,
						10
					)
				elif self.board[row][col] == 'X':
					self.draw_x(row, col)

	def draw_x(self, row, col):
		pygame.draw.line(
			self.window,
			WHITE,
			(col * 200 + 55, row * 200 + 140),
			(col * 200 + 130, row * 200 + 50),
			15
		)

		pygame.draw.line(
			self.window,
			WHITE,
			(col * 200 + 55, row * 200 + 50),
			(col * 200 + 130, row * 200 + 140),
			15
		)
