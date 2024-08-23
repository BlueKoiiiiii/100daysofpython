import pygame
import win32api
import win32con
import win32gui
import pyautogui
import time
import tkinter as tk
import random
import sys
class SpriteSheet():
    def __init__ (self, image):
        self.sheet = image
    def get_image4(self, frame, width, height, scale):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 5, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey((0, 0, 0))
        return image