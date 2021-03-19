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