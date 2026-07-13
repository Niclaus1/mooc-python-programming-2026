# WRITE YOUR SOLUTION HERE:
import pygame
from PIL import Image

pygame.init()
window = pygame.display.set_mode((640, 480))

image = Image.open("robot.png")
image.save("output.bmp")
robot = pygame.image.load("output.bmp")

width = robot.get_width()
height = robot.get_height()

window.fill((0, 0, 0))
for x in range(1, 11):
    window.blit(robot, (20 + (width * x), 100))


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
