import pygame

pygame.init()
pygame.font.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 900, 500
PLAYER_WIDTH, PLAYER_HEIGHT = 55, 40
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BORDER_COLOR = (0, 102, 102)
FPS = 60
PLAYER_SPEED = 3
BULLET_SPEED = 6
MAX_BULLETS = 5

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

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

BORDER = pygame.Rect(WINDOW_WIDTH // 2 - 5, 0, 10, WINDOW_HEIGHT)

LIVES_FONT = pygame.font.SysFont("Arial", 35)
WINNER_FONT = pygame.font.SysFont("Arial", 70)


class Shooter:
	def __init__(self):
		super().__init__()
		self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption("Shooter")
		self.main()

	def main(self):
		yellow = pygame.Rect(50, 230, PLAYER_WIDTH, PLAYER_HEIGHT)
		red = pygame.Rect(795, 230, PLAYER_HEIGHT, PLAYER_WIDTH)

		yellow_bullets = []
		red_bullets = []

		yellow_lives = 3
		red_lives = 3

		clock = pygame.time.Clock()
		run = True
		while run:
			clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					pygame.quit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
						bullet = pygame.Rect(yellow.x + PLAYER_WIDTH, yellow.y + PLAYER_HEIGHT // 2 + 4, 8, 8)
						yellow_bullets.append(bullet)

					if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
						bullet = pygame.Rect(red.x, red.y + PLAYER_HEIGHT // 2 + 4, 8, 8)
						red_bullets.append(bullet)

				if event.type == YELLOW_HIT:
					print("Żółty dostał")
					yellow_lives -= 1
				if event.type == RED_HIT:
					print("Czerwony dostał")
					red_lives -= 1

			winner_text = ""

			if yellow_lives <= 0:
				winner_text = "Red Wins!"
			if red_lives <= 0:
				winner_text = "Yellow Wins!"
			if winner_text != "":
				self.draw_winner(winner_text)
				break

			self.players_movement_handle(yellow, red)
			self.shooting_handle(yellow_bullets, red_bullets, yellow, red, yellow_lives, red_lives)
			self.draw_window(yellow, red, yellow_bullets, red_bullets, yellow_lives, red_lives, winner_text)

		self.main()

	def draw_window(self, yellow, red, yellow_bullets, red_bullets, yellow_lives, red_lives, winner_text):
		self.window.blit(BACKGROUND, (0, 0))
		pygame.draw.rect(self.window, BORDER_COLOR, BORDER)

		yellow_lives_text = LIVES_FONT.render("Lives: " + str(yellow_lives), True, WHITE)
		red_lives_text = LIVES_FONT.render("Lives: " + str(red_lives), True, WHITE)
		self.window.blit(yellow_lives_text, (10, 10))
		self.window.blit(red_lives_text, (WINDOW_WIDTH - red_lives_text.get_width() - 10, 10))

		self.window.blit(YELLOW_PLAYER, (yellow.x, yellow.y))
		self.window.blit(RED_PLAYER, (red.x, red.y))

		# Drawing bullets
		for bullet in yellow_bullets:
			pygame.draw.rect(self.window, YELLOW, bullet)

		for bullet in red_bullets:
			pygame.draw.rect(self.window, RED, bullet)

		pygame.display.update()

	def players_movement_handle(self, yellow: pygame.Rect, red: pygame.Rect):
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

	def shooting_handle(
						self,
						yellow_bullets: [pygame.Rect],
						red_bullets: [pygame.Rect],
						yellow: pygame.Rect,
						red: pygame.Rect,
						yellow_lives,
						red_lives
					):
		for bullet in yellow_bullets:
			bullet.x += BULLET_SPEED
			if red.colliderect(bullet):
				pygame.event.post(pygame.event.Event(RED_HIT))
				yellow_bullets.remove(bullet)
			elif bullet.x >= WINDOW_WIDTH:
				yellow_bullets.remove(bullet)

		for bullet in red_bullets:
			bullet.x -= BULLET_SPEED
			if yellow.colliderect(bullet):
				pygame.event.post(pygame.event.Event(YELLOW_HIT))
				red_bullets.remove(bullet)
			elif bullet.x <= 0:
				red_bullets.remove(bullet)

	def draw_winner(self, winner_text):
		draw_text = WINNER_FONT.render(winner_text, True, WHITE)
		self.window.blit(draw_text,
						 (WINDOW_WIDTH / 2 - draw_text.get_width() / 2,
						  WINDOW_HEIGHT / 2 - draw_text.get_height())
						)
		pygame.display.update()
		pygame.time.delay(5000)

