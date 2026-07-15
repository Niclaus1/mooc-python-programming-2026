import pygame
from PIL import Image

pygame.init()
window = pygame.display.set_mode((640, 480))

image = Image.open("robot.png")
image.save("output.bmp")
robot = pygame.image.load("output.bmp")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    y += velocity
    if velocity > 0 and y + robot.get_height() >= 480:
        velocity = -velocity
    if velocity < 0 and y <= 0:
        velocity = -velocity

    clock.tick(60)
