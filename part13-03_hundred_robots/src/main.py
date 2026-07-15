# WRITE YOUR SOLUTION HERE:
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
for row in range(10):
    for col in range(10):
        window.blit(robot, (30 + row * 30 + col * 40, 30 + row * 20))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
