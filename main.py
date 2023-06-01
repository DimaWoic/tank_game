import pygame
from sprites.tanks import Tank
from controllers.controllers import controllers

pygame.init()

SCREEN_H = 600
SCREEN_W = 600

clock = pygame.time.Clock()

window = pygame.display.set_mode((SCREEN_H, SCREEN_W))
rect = pygame.Rect(300, 500, 40, 40)
tank = Tank(window)
# pygame.draw.rect(window, (255, 255, 255), tank, 0)

while True:
    events = pygame.event.get()
    controllers(events)
    tank.update_position(events)
    window.fill((0, 0, 0))
    # pygame.draw.rect(window, (255, 255, 255), tank, 0)
    tank.output()
    pygame.display.flip()
    clock.tick(30)
