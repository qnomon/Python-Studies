'''from os import startfile
startfile('M:\Download\hastad-nha.mp3')'''

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
