# Snake & Ladder

🎮 A classic Snake and Ladder game with both Command Line Interface (CLI) and Graphical User Interface (GUI) implementations.

## ✨ Features

### CLI Version
- 🎨 **Beautiful Terminal Interface** - Colorful and responsive UI with Rich
- 🎮 **2-4 Player Support** - Play with friends on the same machine
- 🎲 **Animated Dice Rolling** - Visual dice roll animation
- 🐍 **Snake & Ladder Indicators** - Clear visual cues for all game elements

### GUI Version
- 🖥️ **Graphical Interface** - Play with a beautiful Pygame-based UI
- 🎨 **Visual Animations** - Smooth player movements and dice rolls
- 🎮 **Interactive Controls** - Click to roll, intuitive interface
- 🎵 **Sound Effects** - Immersive gameplay experience

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Git (for cloning the repository)

### Quick Start
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

### CLI Version
1. Switch to the CLI branch:
   ```sh
   git checkout cli
   ```

2. Run the CLI version:
   ```sh
   python SnakeAndLadder(CLI).py
   ```

### GUI Version
1. Switch to the main branch:
   ```sh
   git checkout main
   ```

2. Run the GUI version:
   ```sh
   python run_game.py
   ```

## 📖 Game Instructions

### CLI Version
1. **Start the Game**:
   ```sh
   python SnakeAndLadder(CLI).py
   ```

2. **Main Menu**:
   - Select option `1` to start a new game
   - Select option `2` to learn how to play
   - Select `Q` to quit

3. **Game Setup**:
   - Enter the number of players (2-4)
   - Enter each player's name

4. **Gameplay**:
   - Press `Enter` to roll the dice
   - Watch the animated dice roll
   - The game will automatically move your token
   - Land on ladders (🪜) to climb up
   - Avoid snakes (🐍) or slide down
   - First to reach 100 wins!

### GUI Version
1. **Start the Game**:
   ```sh
   python run_game.py
   ```

2. **Main Menu**:
   - Click "Start Game" to begin
   - Click "How to Play" for instructions
   - Click "Quit" to exit

3. **Game Setup**:
   - Select number of players (2-4)
   - Enter player names
   - Choose token colors

4. **Gameplay**:
   - Click the dice to roll
   - Watch your token move automatically
   - Follow on-screen prompts
   - First to reach 100 wins!

### 🎯 Game Rules (Both Versions)
- Players take turns rolling a six-sided die
- Move your token forward the number of spaces shown on the die
- If you land on the bottom of a ladder, climb up to the top
- If you land on a snake's head, slide down to its tail
- To win, you must reach exactly 100
- If your roll would take you past 100, you stay in place

## 📁 Project Structure

```
snake-and-ladder/
├── cli/
│   └── SnakeAndLadder(CLI).py  # CLI version main file
├── gui/
│   ├── run_game.py            # GUI version main file
│   ├── assets/                # Game assets (images, sounds)
│   └── src/                   # Source code for GUI version
├── requirements.txt           # Dependencies
└── README.md                 # This file
```

## 🛠 Dependencies

### CLI Version
- [Rich](https://github.com/Textualize/rich) - Beautiful terminal formatting
- [Colorama](https://pypi.org/project/colorama/) - Cross-platform colored terminal text

### GUI Version
- [Pygame](https://www.pygame.org/) - Game development library
- [Numpy](https://numpy.org/) - For numerical operations
- [Random2](https://pypi.org/project/random2/) - Better random number generation

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  Made with ❤️ by Aryan Arlikar
</div>

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
