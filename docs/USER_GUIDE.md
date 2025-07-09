# Snake & Ladder - User Guide

Welcome to Snake & Ladder! This guide will help you get started with the game and explain all its features.

## 🎮 Game Overview

Snake & Ladder is a classic board game where players race to reach the final square (usually 100) on the game board. Along the way, you'll encounter:

- **Ladders** that help you climb up the board
- **Snakes** that send you sliding down
- **Dice rolls** that determine how many spaces you move

## 🖥️ Getting Started

### System Requirements
- Operating System: Windows, macOS, or Linux
- Python 3.8 or higher
- Pygame 2.5.0 or higher

### Installation
1. Download the latest release from [GitHub](https://github.com/Aryan01b/SnakeAndLadder/releases)
2. Extract the downloaded ZIP file
3. Open a terminal in the extracted folder

## 🎲 How to Play

### Starting the Game
1. Open a terminal in the game directory
2. Run the game:
   ```bash
   python run_game.py
   ```

### Game Controls

| Action                | Keyboard | Mouse           |
|-----------------------|----------|-----------------|
| Roll Dice             | SPACEBAR | Click the dice  |
| Start New Game        | R        | -               |
| Quit Game            | Q or ESC | Close window    |
| Toggle Fullscreen    | F11      | -               |

## 🏆 Game Rules

1. **Players**: 2-4 players can play (Red, Blue, Green, Yellow)
2. **Turns**: Players take turns in order
3. **Winning**: First player to reach exactly square 100 wins
4. **Exact Roll**: Must roll the exact number to reach 100
5. **Snakes & Ladders**:
   - Head of snake → Move to tail
   - Bottom of ladder → Climb to top

## 🎨 Game Interface

### Board Layout
- The game board is a 10x10 grid (1-100)
- Numbers increase from bottom to top in a snake pattern
- Each player is represented by a colored token with their initial

### Information Panel
- Current player's turn
- Dice value
- Game status messages
- Player positions

## 🎯 Tips & Strategies

1. **Early Game**: Focus on reaching ladders to get ahead quickly
2. **Mid Game**: Be cautious of snake heads when you're near them
3. **End Game**: Try to position yourself to land exactly on 100
4. **Risk Management**: Sometimes it's better to take a smaller roll to avoid a snake

## ❓ Frequently Asked Questions

### Q: How do I install the game?
A: See the [Installation](#installation) section above.

### Q: Can I play with more than 4 players?
A: Currently, the game supports up to 4 players.

### Q: How do I report a bug or request a feature?
A: Please open an issue on our [GitHub repository](https://github.com/Aryan01b/SnakeAndLadder/issues).

## 📞 Support

If you need help or have questions, please:
1. Check the [FAQ](#-frequently-asked-questions) section
2. Search the [GitHub Issues](https://github.com/Aryan01b/SnakeAndLadder/issues)
3. Open a new issue if your question hasn't been answered

## 📜 License

This game is open source and available under the MIT License.
