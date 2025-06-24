#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode(size=(600, 480))

    def rum(self):
        while True:
            menu = Menu(self.window)
            menu.rum()
            pass

            # Check for all events
            #for event in pygame.event.get():
            #   if event.type == pygame.QUIT:
            #       pygame.quit()  # close window
            #       quit()  # end pygame
