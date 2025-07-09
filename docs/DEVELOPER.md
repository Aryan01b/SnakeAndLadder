# Developer Documentation

Welcome to the Snake & Ladder development documentation! This guide will help you understand the project structure, setup your development environment, and contribute to the project.

## 📁 Project Structure

```
snake-and-ladder/
├── game/                      # Main game package
│   ├── __init__.py           # Package initialization
│   ├── constants.py          # Game constants and configurations
│   ├── main.py               # Main game class and entry point
│   │
│   ├── core/                 # Core game logic
│   │   ├── __init__.py
│   │   ├── game_logic.py     # Game rules and mechanics
│   │   └── game_state.py     # Game state management
│   │
│   ├── models/               # Data models
│   │   ├── __init__.py
│   │   ├── board.py          # Board and cell logic
│   │   └── player.py         # Player class and movement
│   │
│   └── ui/                   # User interface components
│       ├── __init__.py
│       ├── animations.py     # Animation system
│       ├── board_ui.py       # Board rendering
│       └── sidebar_ui.py     # Game controls and info
│
├── docs/                     # Documentation
│   ├── DEVELOPER.md         # This file
│   └── USER_GUIDE.md        # User documentation
│
├── .github/workflows/        # CI/CD workflows
│   └── pylint.yml           # Pylint configuration
│
├── requirements.txt          # Project dependencies
└── run_game.py              # Game launcher
```

## 🛠️ Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Aryan01b/SnakeAndLadder.git
   cd SnakeAndLadder
   ```

2. **Set up a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

## 🧪 Testing

Run the test suite:
```bash
pytest tests/
```

## 🧹 Linting

This project uses Pylint for code quality. To run the linter:
```bash
pylint game/ tests/
```

## 🧩 Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use type hints for all function parameters and return values
- Keep functions small and focused on a single responsibility
- Write docstrings for all public functions and classes

## 🚀 Running the Game in Development Mode

To run the game with live reload:
```bash
python run_game.py --dev
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributors

- [Your Name](https://github.com/yourusername) - Initial work

## 📚 Resources

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
