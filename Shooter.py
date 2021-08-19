import pygame

WINDOW_SIZE = (900, 500)
PLAYER_SIZE = (55, 40)
RED = (255, 0, 0)
FPS = 60

YELLOW_PLAYER_IMAGE = pygame.image.load('Assets/spaceship_yellow.png')
YELLOW_PLAYER = pygame.transform.rotate(
		pygame.transform.scale(YELLOW_PLAYER_IMAGE, PLAYER_SIZE), 90
	)

RED_PLAYER_IMAGE = pygame.image.load('Assets/spaceship_red.png')
RED_PLAYER = pygame.transform.rotate(
		pygame.transform.scale(RED_PLAYER_IMAGE, PLAYER_SIZE), 270
	)


class Shooter:
	def __init__(self):
		super().__init__()
		self.window = pygame.display.set_mode(WINDOW_SIZE)
		pygame.display.set_caption("Shooter")
		self.main()

	def main(self):
		clock = pygame.time.Clock()
		run = True
		while run:
			clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

			self.draw_window()

		pygame.quit()

	def draw_window(self):
		self.window.fill(RED)
		self.window.blit(YELLOW_PLAYER, (50, 230))
		self.window.blit(RED_PLAYER, (795, 230))
		pygame.display.update()

