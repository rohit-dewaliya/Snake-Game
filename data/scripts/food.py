import pygame
import random

class Food:
    def __init__(self, food_size, size):
        self.size = size
        self.food_size = food_size
        self.color = (255, 0, 0)

        self.get_pos()

    def get_pos(self):
        x = (random.randint(0, self.size[0]) // self.food_size) * self.food_size
        y = (random.randint(0, self.size[1]) // self.food_size) * self.food_size
        self.pos = [x, y]

    def display_food(self, display):
        pygame.draw.rect(display, self.color, (self.pos[0], self.pos[1], self.food_size, self.food_size))