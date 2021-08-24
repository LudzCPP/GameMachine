import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 900, 500
PLAYER_WIDTH, PLAYER_HEIGHT = 20, 100
BALL_WIDTH, BALL_HEIGHT = 15, 15
PLAYER_SPEED = 5
BALL_SPEED = 4
BALL_ACCELERATION = 0.3
POINTS_FONT = pygame.font.SysFont("Arial", 35)
WINNER_FONT = pygame.font.SysFont("Arial", 50)
LEFT_SCORE = pygame.USEREVENT + 1
RIGHT_SCORE = pygame.USEREVENT + 2
SCORE_TO_WIN = 2

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

		left_points = 0
		right_points = 0

		ball = pygame.Rect(WINDOW_WIDTH / 2 - BALL_WIDTH / 2, WINDOW_HEIGHT / 2 - BALL_HEIGHT / 2, BALL_WIDTH, BALL_HEIGHT)
		ball_speed = BALL_SPEED
		ball_direction = [1, -1]

		clock = pygame.time.Clock()

		run = True
		while run:
			clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					pygame.display.quit()
				if event.type == RIGHT_SCORE:
					right_points += 1
					self.reset_positions(left_player, right_player, ball)
					self.draw_window(left_player, right_player, ball, left_points, right_points)
					ball_speed = BALL_SPEED
					if right_points != SCORE_TO_WIN:
						pygame.time.delay(1000)

				if event.type == LEFT_SCORE:
					left_points += 1
					self.reset_positions(left_player, right_player, ball)
					self.draw_window(left_player, right_player, ball, left_points, right_points)
					ball_speed = BALL_SPEED
					if left_points != SCORE_TO_WIN:
						pygame.time.delay(1000)

			winner_text = ""

			if left_points == SCORE_TO_WIN:
				winner_text = "Left player wins!"
			if right_points == SCORE_TO_WIN:
				winner_text = "Right player wins!"
			if winner_text != "":
				self.reset_positions(left_player, right_player, ball)
				self.draw_winner(winner_text)
				break

			self.player_movement_handle(left_player, right_player)
			ball_direction, ball_speed = self.ball_movement_handle(ball, ball_direction, left_player, right_player, ball_speed)
			self.draw_window(left_player, right_player, ball, left_points, right_points)

		self.main()

	def draw_window(self, left, right, ball, l_points, r_points):
		self.window.fill(BLACK)

		left_points = POINTS_FONT.render(f"Score: {l_points}", True, WHITE)
		right_points = POINTS_FONT.render(f"Score: {r_points}", True, WHITE)
		self.window.blit(left_points, (75, 10))
		self.window.blit(right_points, (WINDOW_WIDTH - left_points.get_width() - 75, 10))

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

	def ball_movement_handle(self, ball, direction, left, right, ball_speed):
		ball.x += ball_speed * direction[0]
		ball.y += ball_speed * direction[1]

		# Bouncing
		if ball.y <= 0:
			direction[1] *= -1
		if ball.y >= WINDOW_HEIGHT - BALL_HEIGHT:
			direction[1] *= -1
		if ball.colliderect(left) or ball.colliderect(right):
			direction[0] *= -1
			ball_speed += BALL_ACCELERATION

		#Points
		if ball.x < 0:
			pygame.event.post(pygame.event.Event(RIGHT_SCORE))
		if ball.x > WINDOW_WIDTH - BALL_WIDTH:
			pygame.event.post(pygame.event.Event(LEFT_SCORE))

		return [direction, ball_speed]

	def reset_positions(self, left, right, ball):
		ball.x = WINDOW_WIDTH / 2 - BALL_WIDTH / 2
		ball.y = WINDOW_HEIGHT / 2 - BALL_HEIGHT / 2
		left.x, left.y = 50, WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2
		right.x, right.y = WINDOW_WIDTH - 50 - PLAYER_WIDTH, WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2

	def draw_winner(self, win_text):
		# self.reset_positions()
		winner_text = WINNER_FONT.render(win_text, True, WHITE)
		self.window.blit(winner_text, (WINDOW_WIDTH / 2 - winner_text.get_width() / 2, WINDOW_HEIGHT / 2 - winner_text.get_height() / 2 - 50))
		pygame.display.update()
		pygame.time.delay(5000)
