import pygame
import random

from pygame.locals import *

from data.scripts.font import Font
from data.scripts.clock import Clock
from data.scripts.snake import Snake
from data.scripts.food import Food

pygame.init()

game_start = True


class GameScreen:
    def __init__(self, size=None):
        if size is None:
            size = [960, 540]
        self.SIZE = size

        self.SCREEN = pygame.display.set_mode(self.SIZE, 0, 32)

        self.clock = Clock(30)

        self.size = 20
        self.snake = Snake(self.size, self.SIZE)
        self.food = Food(self.size, self.SIZE)

        self.font = Font('small_font.png', (255, 0, 0), 4)
        self.font1 = Font('small_font.png', (255, 255, 255), 3)

        self.score = 0
        self.game = True

    def game_over(self):
        game = True
        while game:

            self.font.display_fonts(self.SCREEN, f"Score {self.score}", [440, 250])
            self.font1.display_fonts(self.SCREEN, f"Press r to Play", [400, 300])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                    game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_r:
                        self.score = 0
                        self.snake = Snake(self.size, self.SIZE)
                        self.food = Food(self.size, self.SIZE)
                        game = False

            pygame.display.update()
            self.clock.tick()

    def main(self):
        while self.game:
            self.SCREEN.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False

                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT:
                        self.snake.direction = 'left'
                    if event.key == K_RIGHT:
                        self.snake.direction = 'right'
                    if event.key == K_UP:
                        self.snake.direction = 'up'
                    if event.key == K_DOWN:
                        self.snake.direction = 'down'

            if self.snake.direction == 'right':
                self.snake.position[0] += self.snake.speed
            elif self.snake.direction == 'left':
                self.snake.position[0] -= self.snake.speed
            elif self.snake.direction == 'up':
                self.snake.position[1] -= self.snake.speed
            else:
                self.snake.position[1] += self.snake.speed

            if self.snake.get_confirmation(self.food.pos):
                self.food.get_pos()
                self.score += 1
            else:
                self.snake.snake_positions.pop()

            if self.snake.check_collision():
                self.game_over()

            self.snake.snake_positions.insert(0, list(self.snake.position))
            self.snake.display(self.SCREEN)

            self.food.display_food(self.SCREEN)

            if 0 < self.snake.position[0] < self.SIZE[0] and 0 < self.snake.position[1] < self.SIZE[1]:
                pass
            else:
                self.game_over()

            pygame.display.update()
            self.clock.tick()


if __name__ == "__main__":
    game = GameScreen()
    game.game_over()
    if game_start:
        game.main()