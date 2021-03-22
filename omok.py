import pygame as pg
import pygame
import numpy as np

pygame.init()

# Define colors for using
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)


# Set the height and width of screen
size = [400,400]
screen = pg.display.set_mode(size)

pg.display.set_caption("Game-Title")


#Loop until user click the close button
done = False
clock = pg.time.Clock()

while not done:
    # This limits the while loop to the max of 10 times per second
    # Leave this out and we will use all CPU we can
    clock.tick(10)

    #Main Event Loop
    for event in pg.event.get(): # User do something
        if event.type == pg.QUIT: # If use clicked close
            done=True # Flag that we are done so we exit this loop

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # Working part
    pg.draw.polygon(screen,GREEN, [[30,150],[125,100],[220,150]], 5)

    # For update
    # Must happen after working
    pg.display.flip()

# Be IDLE Friendly
pygame.quit

