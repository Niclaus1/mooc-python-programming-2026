import pygame
from PIL import Image

pygame.init()
window = pygame.display.set_mode((640, 480))

image = Image.open("robot.png")
image.save("output.bmp")
robot = pygame.image.load("output.bmp")

x1 = 0
x2 = 0
xVel1 = 1
xVel2 = 10
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x1, 100))
    window.blit(robot, (x2, 300))
    pygame.display.flip()

    x1 += xVel1
    if xVel1 > 0 and x1 + robot.get_width() >= 640:
        xVel1 = -xVel1
    if xVel2 < 0 and x1 <= 0:
        xVel1 = -xVel1

    x2 += xVel2
    if xVel2 > 0 and x2 + robot.get_width() >= 640:
        xVel2 = -xVel2
    if xVel2 < 0 and x2 <= 0:
        xVel2 = -xVel2
    clock.tick(60)
