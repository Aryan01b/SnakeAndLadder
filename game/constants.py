"""Game constants and configurations."""

# Window and Board Configuration
BOARD_WIDTH = 800  # Width of the game board
SIDEBAR_WIDTH = 300  # Width of the sidebar
WINDOW_SIZE = (BOARD_WIDTH + SIDEBAR_WIDTH, 800)  # Total window dimensions
SIDEBAR_X = BOARD_WIDTH  # X position of the sidebar
BOARD_SIZE = 10  # 10x10 board
CELL_SIZE = BOARD_WIDTH // BOARD_SIZE
FPS = 60  # Frames per second for the game loop

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (240, 240, 240)
DARK_GRAY = (100, 100, 100)

# Game Elements
# Snake positions (start: end)
SNAKES = {
    16: 6, 47: 26, 49: 11, 56: 53, 62: 19,
    64: 60, 87: 24, 93: 73, 95: 75, 98: 78
}

# Ladder positions (start: end)
LADDERS = {
    1: 38, 4: 14, 9: 31, 21: 42, 28: 84,
    36: 44, 51: 67, 71: 91, 80: 100
}

# Animation Settings
ANIMATION_DURATION = 500  # milliseconds
DICE_ROLL_DURATION = 1000  # milliseconds

# UI Settings
SIDEBAR_PADDING = 20
DICE_SIZE = 100
PLAYER_RADIUS = 15
