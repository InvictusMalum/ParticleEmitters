import pygame
from pygame.locals import *

from SettingsClasses.Buttons import *
from SettingsClasses.Slider import *
from SettingsClasses.Texts import *
from main import *

class Settings():
   backgroundColor = settingsColor
   panelWidth = SETTINGS_WIDTH
   
   buttons = []
   lists = []
   texts = []
   textBoxes = []
   
   @staticmethod
   def startup():
      emitterButtons = ToggleButtonList()
      emitterButtons.append(ToggleButtonForList(x=SCREEN_WIDTH+Settings.panelWidth/2-75, y=100, w=150, text = "Particle 1"))
      emitterButtons.append(ToggleButtonForList(x=SCREEN_WIDTH+Settings.panelWidth/2-75, y=130, w=150, text = "Particle 2"))
      emitterButtons.append(ToggleButtonForList(x=SCREEN_WIDTH+Settings.panelWidth/2-75, y=160, w=150, text = "Particle 3"))
      emitterButtons.append(ToggleButtonForList(x=SCREEN_WIDTH+Settings.panelWidth/2-75, y=190, w=150, text = "Particle 4"))
      Settings.lists.append(emitterButtons)

   @staticmethod
   def handle_event(event):
      for button in Settings.buttons:
         button.handle_event(event)
      for box in Settings.textBoxes:
         box.handle_event(event)
      for list in Settings.lists:
         list.handle_event(event)
   
   @staticmethod
   def update():
      for button in Settings.buttons:
         button.update()
      for list in Settings.lists:
         list.update()
   
   @staticmethod
   def draw(screen):
      pygame.draw.rect(screen, Settings.backgroundColor, (SCREEN_WIDTH, 0, Settings.panelWidth, SCREEN_HEIGHT), 0)
      pygame.draw.rect(screen, white, (SCREEN_WIDTH+1,0,4,SCREEN_HEIGHT))
      for button in Settings.buttons:
         button.draw(screen)
      for list in Settings.lists:
         list.draw(screen)
      for box in Settings.textBoxes:
         box.draw(screen)
      for text in Settings.texts:
         text.draw(screen)
      
   @staticmethod
   def writeInfo():
      pass
