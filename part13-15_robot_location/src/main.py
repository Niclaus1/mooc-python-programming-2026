import random

import pygame
from PIL import Image

pygame.init()
window = pygame.display.set_mode((640, 480))

image = Image.open("robot.png")
image.save("output.bmp")
robot = pygame.image.load("output.bmp")

target_x = 0
target_y = 0
locX = random.randint(0, 640 - robot.get_width())
locY = random.randint(0, 480 - robot.get_height())
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            target_x = event.pos[0]
            target_y = event.pos[1]
            print(locX, locY)
            print(target_x, target_y)
            if (
                locX <= target_x <= locX + robot.get_width()
                and locY <= target_y <= locY + robot.get_height()
            ):
                locX = random.randint(0, 640 - robot.get_width())
                locY = random.randint(0, 480 - robot.get_height())

        if event.type == pygame.QUIT:
            exit(0)

    window.fill((0, 0, 0))
    window.blit(robot, (locX, locY))

    pygame.display.flip()

    clock.tick(60)
