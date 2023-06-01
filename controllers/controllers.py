import pygame
import sys
def controllers(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)