import pygame
import os
import time
import random

width = 950
height = 650

# Window
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Jet Fighter")

# Colors
col_grey = (95, 96, 95)

# Images and coordinates
black_ship = pygame.transform.scale(pygame.image.load(os.path.join("assets", "black_ship.png")), (32, 32))
white_ship = pygame.transform.scale(pygame.image.load(os.path.join("assets", "white_ship.png")), (32, 32))

# Entities
class Player:
  def __init__(self, image, x, y):
    self.y = y
    self.x = x
    self.image = image
    self.spd = 2
  def show(self):
    window.blit(self.image, (self.x, self.y))
  def move(self):
    self.y -= self.spd

# Instances
white = Player(white_ship, width - 150, 300)
black = Player(black_ship, 100, 300)

# Game loop
def main():
  run = True
  fps = 60
  clock = pygame.time.Clock()
  def redraw():
    window.fill(col_grey)
    black.show()
    white.show()
    black.move()
    white.move()
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
        if e.key == pygame.K_RIGHT:
          print("pressed k_right")
main()