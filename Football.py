import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 900, 500
PLAYER_WIDTH, PLAYER_HEIGHT = 20, 100
BALL_WIDTH, BALL_HEIGHT = 15, 15
BALL_SPEED = 5
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
		ball = pygame.Rect(WINDOW_WIDTH / 2 - BALL_WIDTH / 2, WINDOW_HEIGHT / 2 - BALL_HEIGHT / 2, BALL_WIDTH, BALL_HEIGHT)

		ball_direction = [1, -1]

		clock = pygame.time.Clock()

		run = True
		while run:
			clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					pygame.display.quit()

			self.player_movement_handle(left_player, right_player)
			ball_direction = self.ball_movement_handle(ball, ball_direction, left_player, right_player)
			self.draw_window(left_player, right_player, ball)

	def draw_window(self, left, right, ball):
		self.window.fill(BLACK)
		pygame.draw.rect(self.window, WHITE, left)
		pygame.draw.rect(self.window, WHITE, right)
		pygame.draw.rect(self.window, WHITE, ball)

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

	def ball_movement_handle(self, ball, direction, left, right):
		ball.x += BALL_SPEED * direction[0]
		ball.y += BALL_SPEED * direction[1]

		if ball.y <= 0:
			direction[1] *= -1
		if ball.y >= WINDOW_HEIGHT - BALL_HEIGHT:
			direction[1] *= -1
		if ball.colliderect(left) or ball.colliderect(right):
			direction[0] *= -1

		return direction
