# Snake & Ladder

A classic Snake and Ladder game implemented in Python with both Command Line Interface (CLI) and Pygame-based Graphical User Interface (GUI).

## Features

### Player Experience
- 🎮 **Interactive GUI**: Play with a beautiful graphical interface
- 🖥️ **Command Line Interface**: Play directly in your terminal
- 🎲 **Smooth Animations**: Enjoy fluid player movements and dice rolls
- 🎨 **Visual Feedback**: Clear indicators for snakes, ladders, and player turns

### Game Modes
- **Single Player**: Play against the computer
- **Multiplayer**: Play with friends on the same device

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Pygame 2.5.0 or higher

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/Aryan01b/SnakeAndLadder.git
   cd SnakeAndLadder
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## 🎮 How to Play

### GUI Mode (Recommended)
To start the game with the graphical interface:
```sh
python run_game.py
```

#### Controls
- **Roll Dice**: Click the dice or press `SPACEBAR`
- **New Game**: Press `R`
- **Quit**: Press `Q` or `ESC`

### CLI Mode
To play in the terminal:
```sh
python snake_and_ladder_cli.py
```

## 📚 Documentation

- [User Guide](docs/USER_GUIDE.md) - Complete guide to playing the game
- [Developer Documentation](docs/DEVELOPER.md) - Technical details for developers

## 🛠️ Development

Interested in contributing? Check out our [Developer Documentation](docs/DEVELOPER.md) for setup instructions, code structure, and contribution guidelines.
```sh
python snake_and_ladder_pygame.py
```

### Rules
- Players take turns to roll a dice.
- The player moves forward based on the dice number.
- If a player lands on the bottom of a ladder, they move up to the top of the ladder.
- If a player lands on the head of a snake, they move down to the tail of the snake.
- The first player to reach the last square on the board wins.

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

### License
This project is licensed under the MIT License.

### Contact
For any questions or feedback, feel free to open an issue or contact the repository owner.
