import pygame
from PIL import Image

pygame.init()
window = pygame.display.set_mode((640, 480))

image = Image.open("robot.png")
image.save("output.bmp")
robot = pygame.image.load("output.bmp")

x = 0
y = 0
xVelocity = 1
yVelocity = 1
clock = pygame.time.Clock()

right = True
down = False
left = False
up = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    if right:
        x += xVelocity
        down = False
        if x + robot.get_width() >= 640:
            right = False
            down = True

    if down:
        y += yVelocity
        if y + robot.get_height() >= 480:
            down = False
            left = True
    if left:
        x -= xVelocity
        if x <= 0:
            left = False
            up = True

    if up:
        y -= yVelocity
        if y <= 0:
            up = False
            right = True

    clock.tick(60)
