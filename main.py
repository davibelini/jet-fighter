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
# game
def main():
  run = True
  fps = 60
  clock = pygame.time.Clock()
  def redraw_window():
    window.fill(col_grey)
    pygame.display.update()
  while run:
    clock.tick(fps)
    redraw_window()
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
            run = False
main()