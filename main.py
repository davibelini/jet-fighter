import pygame
import os
import time
import random

# setup
width = 950
height = 650
col_grey = (95, 96, 95)
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Jet Fighter")
###
# sprites
black_ship = pygame.transform.scale(pygame.image.load(os.path.join("assets", "black_ship.png")), (32, 32))
left_start_coord = (100, 300)
white_ship = pygame.transform.scale(pygame.image.load(os.path.join("assets", "white_ship.png")), (32, 32))
right_start_coord = (width - 150, 300)
###
# data
black_ship_angle = 0
###
# game
def main():
  global black_ship_angle
  run = True
  fps = 60
  clock = pygame.time.Clock()
  def redraw():
    window.fill(col_grey)
    window.blit(black_ship, left_start_coord)
    window.blit(white_ship, right_start_coord)
    pygame.display.update()
  while run:
    clock.tick(fps)
    redraw()
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        run = False
      if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_LEFT:
          print("pressed k_left")
          # pygame.transform.rotate(black_ship, black_ship_angle) # it's not working
          black_ship_angle += 1
main()