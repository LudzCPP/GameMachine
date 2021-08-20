import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 900, 500
PLAYER_WIDTH, PLAYER_HEIGHT = 55, 40
RED = (255, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
PLAYER_SPEED = 3

YELLOW_PLAYER_IMAGE = pygame.image.load('Assets/spaceship_yellow.png')
YELLOW_PLAYER = pygame.transform.rotate(
		pygame.transform.scale(YELLOW_PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 90
	)

RED_PLAYER_IMAGE = pygame.image.load('Assets/spaceship_red.png')
RED_PLAYER = pygame.transform.rotate(
		pygame.transform.scale(RED_PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 270
	)

BACKGROUND_IMAGE = pygame.image.load('Assets/background_space.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (WINDOW_WIDTH, WINDOW_HEIGHT))

BORDER = pygame.Rect(WINDOW_WIDTH / 2 - 5, 0, 10, WINDOW_HEIGHT)


class Shooter:
	def __init__(self):
		super().__init__()
		self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption("Shooter")
		self.main()

	def main(self):
		yellow = pygame.Rect(50, 230, PLAYER_WIDTH, PLAYER_HEIGHT)
		red = pygame.Rect(795, 230, PLAYER_HEIGHT, PLAYER_WIDTH)

		clock = pygame.time.Clock()
		run = True
		while run:
			clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

			self.players_movement_handler(yellow, red)
			self.draw_window(yellow, red)
		pygame.quit()

	def draw_window(self, yellow: pygame.Rect, red: pygame.Rect):
		self.window.blit(BACKGROUND, (0, 0))
		pygame.draw.rect(self.window, WHITE, BORDER)
		self.window.blit(YELLOW_PLAYER, (yellow.x, yellow.y))
		self.window.blit(RED_PLAYER, (red.x, red.y))
		pygame.display.update()

	def players_movement_handler(self, yellow: pygame.Rect, red: pygame.Rect):
		keys_pressed = pygame.key.get_pressed()
		# Red Player
		if keys_pressed[pygame.K_UP] and red.y >= 0:
			red.y -= PLAYER_SPEED
		if keys_pressed[pygame.K_DOWN] and red.y <= WINDOW_HEIGHT - PLAYER_HEIGHT + PLAYER_SPEED - 20:
			red.y += PLAYER_SPEED
		if keys_pressed[pygame.K_LEFT] and red.x >= BORDER.x + 15:
			red.x -= PLAYER_SPEED
		if keys_pressed[pygame.K_RIGHT] and red.x <= WINDOW_WIDTH - PLAYER_WIDTH + PLAYER_SPEED + 9:
			red.x += PLAYER_SPEED

		# Yellow Player
		if keys_pressed[pygame.K_w] and yellow.y >= 0:
			yellow.y -= PLAYER_SPEED
		if keys_pressed[pygame.K_s] and yellow.y <= WINDOW_HEIGHT - PLAYER_HEIGHT + PLAYER_SPEED - 20:
			yellow.y += PLAYER_SPEED
		if keys_pressed[pygame.K_a] and yellow.x >= 0:
			yellow.x -= PLAYER_SPEED
		if keys_pressed[pygame.K_d] and yellow.x <= BORDER.x - PLAYER_WIDTH + PLAYER_SPEED + 9:
			yellow.x += PLAYER_SPEED
