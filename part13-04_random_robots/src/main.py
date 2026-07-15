# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import random

import pygame
from PIL import Image

pygame.init()
window = pygame.display.set_mode((800, 480))

image = Image.open("robot.png")
image.save("output.bmp")
robot = pygame.image.load("output.bmp")

width = robot.get_width()
height = robot.get_height()

window.fill((0, 0, 0))
for row in range(1000):
    x = random.randint(1, 1000)
    y = random.randint(1, 1000)
    window.blit(robot, (x, y))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
