import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600
BORDER_WIDTH = 10
BORDER = [
	pygame.Rect(WINDOW_WIDTH / 3 - BORDER_WIDTH / 2, 0, BORDER_WIDTH, WINDOW_HEIGHT),
	pygame.Rect(2 * (WINDOW_WIDTH / 3) - BORDER_WIDTH / 2, 0, BORDER_WIDTH, WINDOW_HEIGHT),
	pygame.Rect(0, WINDOW_HEIGHT / 3 - BORDER_WIDTH / 2, WINDOW_WIDTH, BORDER_WIDTH),
	pygame.Rect(0, 2 * (WINDOW_HEIGHT / 3 - BORDER_WIDTH / 2), WINDOW_WIDTH, BORDER_WIDTH)
]

WINNING_COMBINATIONS = [
	[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]],
	[[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]],
	[[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]
]

GAME_END = pygame.USEREVENT + 1

SIGNS = {
	True: 'X',
	False: 'O'
}

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

board = []


class TicTacToe:
	def __init__(self):
		self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.current_sign = True
		pygame.display.set_caption("Tic Tac Toe")
		self.main()

	def main(self):
		clock = pygame.time.Clock()

		global board

		board = [
			['-', '-', '-'],
			['-', '-', '-'],
			['-', '-', '-']
		]

		run = True
		while run:
			clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					pygame.display.quit()
				if event.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()
					self.click_handle(pos)
				if event.type == GAME_END:
					pygame.time.delay(3000)
					board = [
						['-', '-', '-'],
						['-', '-', '-'],
						['-', '-', '-']
					]

			self.draw_window()

	def draw_window(self):
		self.window.fill(BLACK)
		for rect in BORDER:
			pygame.draw.rect(self.window, WHITE, rect)

		self.draw_shapes()

		pygame.display.update()

	def click_handle(self, pos):
		global board

		col = int(pos[0] // (WINDOW_WIDTH / 3 - BORDER_WIDTH / 2))
		row = int(pos[1] // (WINDOW_HEIGHT / 3 - BORDER_WIDTH / 2))

		if board[row][col] == '-':
			board[row][col] = SIGNS[self.current_sign]
			self.current_sign = not self.current_sign

		if self.check_win():
			self.win_handle(self.check_win())

	def draw_shapes(self):
		global board

		for row in range(3):
			for col in range(3):
				if board[row][col] == 'O':
					pygame.draw.circle(
						self.window,
						WHITE,
						(col * 200 + 100, row * 200 + 100),
						50,
						10
					)
				elif board[row][col] == 'X':
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

	def check_win(self):
		global board

		for comb in WINNING_COMBINATIONS:
			if board[comb[0][0]][comb[0][1]] == board[comb[1][0]][comb[1][1]] == board[comb[2][0]][comb[2][1]] != '-':
				return comb
		return False

	def win_handle(self, comb):
		global board

		for row in range(3):
			for col in range(3):
				if [row, col] not in comb:
					board[row][col] = '-'

		pygame.display.update()

		pygame.event.post(pygame.event.Event(GAME_END))



