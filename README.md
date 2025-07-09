# Snake & Ladder (CLI Version)

🐍 A beautiful and feature-rich command-line implementation of the classic Snake and Ladder game, built with Python and Rich.

## ✨ Features

- 🎨 **Beautiful Terminal Interface** - Colorful and responsive UI with Rich
- 🎮 **2-4 Player Support** - Play with friends on the same machine
- 🎲 **Animated Dice Rolling** - Visual dice roll animation
- 🐍 **Snake & Ladder Indicators** - Clear visual cues for all game elements
- 🔄 **Interactive Gameplay** - Simple and intuitive controls
- 🏆 **Win Detection** - Automatic winner announcement
- 🔄 **Play Again** - Quick restart option after game ends

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher

### Quick Start
1. Clone the repository and switch to the CLI branch:
   ```sh
   git clone https://github.com/Aryan01b/SnakeAndLadder.git
   cd SnakeAndLadder
   git checkout cli
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Start the game:
   ```sh
   python SnakeAndLadder(CLI).py
   ```

## 🎮 How to Play

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

### 🎯 Game Rules
- Players take turns rolling a six-sided die
- Move your token forward the number of spaces shown on the die
- If you land on the bottom of a ladder, climb up to the top
- If you land on a snake's head, slide down to its tail
- To win, you must reach exactly 100
- If your roll would take you past 100, you stay in place

## 📁 Project Structure

```
snake-and-ladder/
├── SnakeAndLadder(CLI).py  # Main game file
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## 🛠 Dependencies

- [Rich](https://github.com/Textualize/rich) - Beautiful terminal formatting
- [Colorama](https://pypi.org/project/colorama/) - Cross-platform colored terminal text

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
