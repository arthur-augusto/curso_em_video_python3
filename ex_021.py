# Toca um mp3 usando a biblioteca pygame
import pygame
pygame.init()
pygame.mixer.music.load('ex_021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
