# Snake Game 🐍

A simple Snake Game implemented in Python using the `turtle` module.

## 🎮 How to Play
- Use the arrow keys (`Up`, `Down`, `Left`, `Right`) to move the snake.
- Eat the food (blue dot) to grow the snake and increase the score.
- The game ends when the snake collides with the wall or itself.

## 🏆 High Score Feature
- The game keeps track of the highest score by storing it in `data.txt`.
- If the player's score exceeds the previous high score, it is saved automatically.
- When restarting the game, the high score is loaded from `data.txt`.

## 🛠️ Requirements
- Python 3.x
- `turtle` (included in Python's standard library)

## 📝 Files Overview
- `main.py` - The entry point of the game.
- `snake.py` - The Snake class handling movement and growth.
- `food.py` - The Food class for random food placement.
- `scoreboard.py` - The Score class for tracking the score and displaying game over.
- `data.txt` - Stores the highest score recorded.

## 🚀 How to Run the Game
1. Navigate to the folder
2. Run the main.py