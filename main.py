import pygame
import os
import time
import random

# setup
width = 850
height = 700
col_grey = (95, 96, 95)
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Jet Fighter")
###
# import sprites
black_ship = pygame.image.load(os.path.join("assets", "black_ship.png"))
###
# game
def main():
  run = True
  fps = 60
  clock = pygame.time.Clock()
  def redraw():
    window.fill(col_grey)
    pygame.display.update()
  while run:
    clock.tick(fps)
    redraw()
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
            run = False
main()