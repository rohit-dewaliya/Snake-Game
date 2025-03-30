# Snake Game


A simple Snake game built using Python and Pygame.

---

## Screenshots
![Screenshot 2025-03-30 160757.png](data/photos/Screenshot%202025-03-30%20160757.png)
![Screenshot 2025-03-30 160901.png](data/photos/Screenshot%202025-03-30%20160901.png)
![Screenshot 2025-03-30 160912.png](data/photos/Screenshot%202025-03-30%20160912.png)
---
## Features

- Classic snake movement
- Food spawning at random positions
- Score tracking
- Game-over screen with restart option
- Snake size increases when food is eaten

---
## Requirements

Make sure you have Python installed on your system. You also need Pygame:

```sh
pip install pygame
```

---
## How to Run

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/snake-game.git
   cd snake-game
   ```

2. Run the game:

   ```sh
   python main.py
   ```
---
## Controls

- **Arrow Keys**: Move the snake (Up, Down, Left, Right)
- **R Key**: Restart after game over
- **ESC**: Quit the game

---
## Game Rules

- Eat food to grow longer
- Avoid colliding with the walls or yourself
- The game ends if you hit a wall or your own body

---
## Snake Size Increment Logic

When the snake eats food:

1. The game checks if the snake's head position matches the food's position.
2. If a match is found, a new food position is generated.
3. The score is increased.
4. The snake does **not** remove its tail (which normally happens on movement), effectively increasing its length.

```python
if self.snake.get_confirmation(self.food.pos):  # Eating food
    self.food.get_pos()  # Generate new food position
    self.score += 1  # Increase score
else:
    self.snake.snake_positions.pop()  # Remove tail to maintain length
```

---
## File Structure

```
/
├── data/
│   ├── scripts/
│   │   ├── font.py
│   │   ├── clock.py
│   │   ├── snake.py
│   │   ├── food.py
│   ├── assets/
├── main.py
├── README.md
```

---