import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 900, 500
PLAYER_WIDTH, PLAYER_HEIGHT = 20, 100
PLAYER_SPEED = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60


class Football:
	def __init__(self):
		self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption("Football")
		self.main()

	def main(self):
		left_player = pygame.Rect(50, WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2, PLAYER_WIDTH, PLAYER_HEIGHT)
		right_player = pygame.Rect(WINDOW_WIDTH - 50 - PLAYER_WIDTH, WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2, PLAYER_WIDTH, PLAYER_HEIGHT)

		clock = pygame.time.Clock()

		run = True
		while run:
			clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					pygame.display.quit()

			self.player_movement_handle(left_player, right_player)
			self.draw_window(left_player, right_player)

	def draw_window(self, left, right):
		self.window.fill(BLACK)
		pygame.draw.rect(self.window, WHITE, left)
		pygame.draw.rect(self.window, WHITE, right)
		pygame.display.update()

	def player_movement_handle(self, left, right):
		pressed_keys = pygame.key.get_pressed()

		if pressed_keys[pygame.K_w] and left.y > 0:
			left.y -= PLAYER_SPEED
		if pressed_keys[pygame.K_s] and left.y < WINDOW_HEIGHT - PLAYER_HEIGHT:
			left.y += PLAYER_SPEED
		if pressed_keys[pygame.K_UP] and right.y > 0:
			right.y -= PLAYER_SPEED
		if pressed_keys[pygame.K_DOWN] and right.y < WINDOW_HEIGHT - PLAYER_HEIGHT:
			right.y += PLAYER_SPEED
