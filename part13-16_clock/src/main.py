from datetime import datetime
from math import cos, radians, sin

import pygame

pygame.init()
display = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
display = pygame.display.set_mode((640, 480))

center = (320, 240)
second = 200
minute = 150
hour = 100


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
    display.fill((0, 0, 0))

    now = datetime.now()
    second_time = now.strftime("%H:%M:%S")[6:8]
    minute_time = now.strftime("%H:%M:%S")[3:5]
    pygame.display.set_caption(now.strftime("%H:%M:%S"))

    sec_angle = 90 - 6 * now.second
    min_angle = 90 - 6 * (now.minute + now.second / 60)
    hour_angle = 90 - 30 * ((now.hour % 12) + now.minute / 60 + now.second / 3600)

    secX = center[0] + second * cos(radians(sec_angle))
    secY = center[1] - second * sin(radians(sec_angle))

    minX = center[0] + minute * cos(radians(min_angle))
    minY = center[1] - minute * sin(radians(min_angle))

    hrX = center[0] + hour * cos(radians(hour_angle))
    hrY = center[1] - hour * sin(radians(hour_angle))

    pygame.draw.circle(display, (255, 0, 0), center, 200, 2)
    # Second
    pygame.draw.line(display, (0, 0, 255), center, (secX, secY), 1)
    # Minute
    pygame.draw.line(display, (0, 0, 255), center, (minX, minY), 2)
    # Hour
    pygame.draw.line(display, (0, 0, 255), center, (hrX, hrY), 3)

    sec_angle = (sec_angle - 2) % 360
    if int(second_time) == 00:
        min_angle = (min_angle - 2) % 360
    if int(minute_time) == 00:
        hour_angle = (hour_angle - 2) % 360

    pygame.display.flip()
    clock.tick(1)
