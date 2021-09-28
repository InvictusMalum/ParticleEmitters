from Emitters import ParticleBase
import math
import random
import time

import pygame
from pygame.locals import *

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SETTINGS_WIDTH = 300
settingsColor = (100,100,200)

white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
blue = (0, 0, 255)
background = black

pygame.font.init()
defaultFont = pygame.font.SysFont('Times New Roman', 20)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH + SETTINGS_WIDTH, SCREEN_HEIGHT))

def main():
    from SettingsClasses.Settings import Settings
    Settings.startup()

    from Emitters import EmitterBase
    from Emitters import ParticleBase

    emitter = EmitterBase(100,100,10, ParticleBase(1,100,(100,100,100),100,5))

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            Settings.handle_event(event)
            
        screen.fill(background)

        Settings.update()
        Settings.draw(screen)
        Settings.writeInfo()

        emitter.update()
        emitter.draw(screen)

        pygame.display.update()
        
        time.sleep(.001)

if __name__ == "__main__":
    main()
