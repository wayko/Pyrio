import pygame
from settings import *
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Main Menu")
game_paused = True
font = pygame.font.SysFont("arialblack", 40)

text_col = (255,255,255)
def draw_text(text, font, text_col, x ,y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x,y))
run = True
while run:
	screen.fill((52,78,91))
	if game_paused == True:
		draw_text("Press Space To Start", font, text_col, 160, 250)
		
		pygame.display.update()
	else:
		draw_text("Press Space To Return", font, text_col, 160, 250)
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				game_paused = False
		if event.type == pygame.QUIT:
			run = False
		pygame.display.update()
pygame.quit()