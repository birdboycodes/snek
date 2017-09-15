import pygame
#from snake import Snake
import random

pygame.init()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


#bootstrap code from @bypie5
size = [320,240] #[1280,960] [320, 240]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

draw_rate = 15

running = True
clock = pygame.time.Clock()

#snake = Snake(size, 4)
#movement constants
y_dis = 10
x_dis = 10

#Main loop
while running:
	clock.tick(draw_rate)

	#Event checking
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False

	screen.fill((255,255,255))

	#Draw calls
	#snake
	snek_seg = pygame.draw.rect(screen, RED, [x_dis, y_dis, 30, 20])
	x_dis +=1
	


	pygame.display.flip()


pygame.quit()