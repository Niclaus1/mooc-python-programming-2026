# WRITE YOUR SOLUTION HERE:
import pygame
from PIL import Image

pygame.init()
window = pygame.display.set_mode((640, 480))

image = Image.open("robot.png")
image.save("output.bmp")
robot = pygame.image.load("output.bmp")

x = 0
y = 480 - robot.get_height()

to_right = False
to_left = False
to_up = False
to_down = False

x2 = 0
y2 = 480 - robot.get_height()

to_right2 = False
to_left2 = False
to_up2 = False
to_down2 = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_DOWN:
                to_down = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_a:
                to_left2 = True
            if event.key == pygame.K_d:
                to_right2 = True
            if event.key == pygame.K_s:
                to_down2 = True
            if event.key == pygame.K_w:
                to_up2 = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_DOWN:
                to_down = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_a:
                to_left2 = False
            if event.key == pygame.K_d:
                to_right2 = False
            if event.key == pygame.K_s:
                to_down2 = False
            if event.key == pygame.K_w:
                to_up2 = False
        if event.type == pygame.QUIT:
            exit()

    if to_right:
        if not (x + robot.get_width() >= 640):
            x += 2
    if to_left:
        if not (x <= 0):
            x -= 2
    if to_down:
        if not (y + robot.get_height() >= 480):
            y += 2
    if to_up:
        if not (y <= 0):
            y -= 2

    # ------- 2nd Robot -------- #
    if to_right2:
        if not (x2 + robot.get_width() >= 640):
            x2 += 2
    if to_left2:
        if not (x2 <= 0):
            x2 -= 2
    if to_down2:
        if not (y2 + robot.get_height() >= 480):
            y2 += 2
    if to_up2:
        if not (y2 <= 0):
            y2 -= 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)
