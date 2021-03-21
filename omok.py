import pygame as pg
import numpy as np

pygame.init()

# Define colors for using


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
    for event in pygame.event.get(): # User do something
        if event.type == pygame.QUIT: # If use clicked close
            done=True # Flag that we are done so we exit this loop