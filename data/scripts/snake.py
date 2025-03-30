import pygame

class Snake:
    def __init__(self, size, screen_size):
        self.size = size
        self.position = [(screen_size[0] - self.size) // 2, (screen_size[1] - self.size) // 2]

        self.snake_positions = [self.position]
        self.color = (255, 255, 255)
        self.direction = "right"
        self.speed = 5

    def display(self, display):
        for block in self.snake_positions:
            pygame.draw.rect(display, self.color, ((block[0] // self.size) * self.size, (block[1] // self.size) *
                                                   self.size, self.size, self.size))

    def get_confirmation(self, food_pos):
        if [(self.position[0] // self.size) * self.size, (self.position[1] // self.size) * self.size] == food_pos:
            return True
        return False

    def check_collision(self):
        if [(self.position[0] // self.size) * self.size, (self.position[1] // self.size) * self.size] in self.snake_positions[1 : ]:
            return True
        return False