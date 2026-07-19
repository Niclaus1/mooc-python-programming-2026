# WRITE YOUR SOLUTION HERE:
import pygame
from PIL import Image

pygame.init()
window = pygame.display.set_mode((640, 480))

image = Image.open("ball.png")
image.save("output.bmp")
robot = pygame.image.load("output.bmp")

x = 0
y = 0
xVelocity = 1
yVelocity = 1
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    y += yVelocity
    if yVelocity > 0 and y + robot.get_height() >= 480:
        yVelocity = -yVelocity
    if yVelocity < 0 and y <= 0:
        yVelocity = -yVelocity

    x += xVelocity
    if xVelocity > 0 and x + robot.get_width() >= 640:
        xVelocity = -xVelocity
    if yVelocity < 0 and y <= 0:
        xVelocity = -xVelocity

    clock.tick(60)
