## Snake-n-Ladder

This is a Snake and Ladder game implemented in Python with both CLI and Pygame interfaces.

### Features
- **Command Line Interface (CLI)**: Play the game directly in your terminal.
- **Pygame Interface**: Enjoy a graphical version of the game using Pygame.

### Installation
To run this game, you need to have Python and Pygame installed on your system. Follow the steps below:

1. Clone the repository:
    ```sh
    git clone https://github.com/Aryan01b/SnakeAndLadder.git
    cd SnakeAndLadder
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### How to Play
You can choose to play the game in either CLI mode or Pygame mode.

#### CLI Mode
To start the game in CLI mode, run:
```sh
python snake_and_ladder_cli.py
```

#### Pygame Mode
To start the game in Pygame mode, run:
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
