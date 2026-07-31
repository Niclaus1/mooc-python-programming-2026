# WRITE YOUR SOLUTION HERE:
import random

import pygame
from PIL import Image

pygame.init()
window = pygame.display.set_mode((640, 480))

image = Image.open("robot.png")
image.save("output.bmp")
robot = pygame.image.load("output.bmp")

image2 = Image.open("rock.png")
image2.save("output2.bmp")
rock = pygame.image.load("output2.bmp")

x = 0
y = 480 - robot.get_height()
to_right = False
to_left = False

clock = pygame.time.Clock()
rocks = []
for _ in range(100):
    rocks.append(
        {
            "x": random.randint(0, int(640 - robot.get_width())),
            "y": random.randint(-10000, 0),
            "down": True,
            "xVelocity": 1,
        }
    )
while True:
    window.fill((0, 0, 0))
    game_font = pygame.font.SysFont("Arial", 24)
    text = game_font.render("Moikka!", True, (255, 0, 0))

    for r in rocks:
        if r["down"]:
            r["y"] += 1
        window.blit(rock, (r["x"], r["y"]))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

        if event.type == pygame.QUIT:
            exit()

    if to_right and not (x + robot.get_width() >= 640):
        x += 2
    if to_left and not (x <= 0):
        x -= 2

    window.blit(robot, (x, y))
    window.blit(text, (x, y))
    pygame.display.flip()

    clock.tick(60)
