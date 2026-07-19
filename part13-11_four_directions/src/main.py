# WRITE YOUR SOLUTION HERE:
import random

import pygame
from PIL import Image

pygame.init()
window = pygame.display.set_mode((640, 480))

image = Image.open("robot.png")
image.save("output.bmp")
robot = pygame.image.load("output.bmp")

clock = pygame.time.Clock()

down = True
right = False
left = False
robots = []

for _ in range(100):
    robots.append(
        {
            "x": random.randint(0, int(640 - robot.get_width())),
            "y": random.randint(-10000, 0),
            "down": True,
            "right": False,
            "left": False,
            "xVelocity": 1,
        }
    )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    for r in robots:
        if r["down"]:
            r["y"] += 1
            if r["y"] + robot.get_height() >= 480 and r["x"] > 320:
                r["down"] = False
                r["right"] = True
            elif r["y"] + robot.get_height() >= 480 and r["x"] < 320:
                r["down"] = False
                r["left"] = True
        if r["right"]:
            r["x"] += 1
        if r["left"]:
            r["x"] -= 1
        window.blit(robot, (r["x"], r["y"]))
    pygame.display.flip()
    clock.tick(60)
