# WRITE YOUR SOLUTION HERE:
import math

import pygame
from PIL import Image

pygame.init()
window = pygame.display.set_mode((640, 480))

image = Image.open("robot.png")
image.save("output.bmp")
robot = pygame.image.load("output.bmp")

clock = pygame.time.Clock()

angle0 = 0
angle1 = 2 * math.pi / 9
angle2 = 4 * math.pi / 9
angle3 = 6 * math.pi / 9
angle4 = 8 * math.pi / 9
angle5 = 10 * math.pi / 9
angle6 = 12 * math.pi / 9
angle7 = 14 * math.pi / 9
angle8 = 16 * math.pi / 9
angle9 = 18 * math.pi / 9


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))

    x = 320 + math.cos(angle0) * 150 - robot.get_width() / 2
    y = 240 + math.sin(angle0) * 150 - robot.get_height() / 2

    x1 = 320 + math.cos(angle1) * 150 - robot.get_width() / 2
    y1 = 240 + math.sin(angle1) * 150 - robot.get_height() / 2

    x2 = 320 + math.cos(angle2) * 150 - robot.get_width() / 2
    y2 = 240 + math.sin(angle2) * 150 - robot.get_height() / 2

    x3 = 320 + math.cos(angle3) * 150 - robot.get_width() / 2
    y3 = 240 + math.sin(angle3) * 150 - robot.get_height() / 2

    x4 = 320 + math.cos(angle4) * 150 - robot.get_width() / 2
    y4 = 240 + math.sin(angle4) * 150 - robot.get_height() / 2

    x5 = 320 + math.cos(angle5) * 150 - robot.get_width() / 2
    y5 = 240 + math.sin(angle5) * 150 - robot.get_height() / 2

    x6 = 320 + math.cos(angle6) * 150 - robot.get_width() / 2
    y6 = 240 + math.sin(angle6) * 150 - robot.get_height() / 2

    x7 = 320 + math.cos(angle7) * 150 - robot.get_width() / 2
    y7 = 240 + math.sin(angle7) * 150 - robot.get_height() / 2

    x8 = 320 + math.cos(angle8) * 150 - robot.get_width() / 2
    y8 = 240 + math.sin(angle8) * 150 - robot.get_height() / 2

    x9 = 320 + math.cos(angle9) * 150 - robot.get_width() / 2
    y9 = 240 + math.sin(angle9) * 150 - robot.get_height() / 2

    window.blit(robot, (x, y))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    window.blit(robot, (x3, y3))
    window.blit(robot, (x4, y4))
    window.blit(robot, (x5, y5))
    window.blit(robot, (x6, y6))
    window.blit(robot, (x7, y7))
    window.blit(robot, (x8, y8))
    window.blit(robot, (x9, y9))
    pygame.display.flip()

    angle0 += 0.01
    angle1 += 0.01
    angle2 += 0.01
    angle3 += 0.01
    angle4 += 0.01
    angle5 += 0.01
    angle6 += 0.01
    angle7 += 0.01
    angle8 += 0.01
    angle9 += 0.01

    clock.tick(60)
