"""Player model for the Snake and Ladder game."""

import pygame
from typing import Tuple, Optional

class Player:
    """Represents a player in the Snake and Ladder game.
    
    Attributes:
        name: The player's name
        color: The player's color as an RGB tuple
        position: The current position on the board (1-100)
        rect: The pygame Rect representing the player's position on screen
    """
    
    def __init__(self, name: str, color: Tuple[int, int, int], position: int = 0):
        """Initialize a new player.
        
        Args:
            name: The player's name
            color: The player's color as an RGB tuple
            position: Starting position (default: 0 - off board)
        """
        self.name = name
        self.color = color
        self.position = position
        self.rect = pygame.Rect(0, 0, 30, 30)  # Will be updated during rendering
        self.target_position = position
        self.is_animating = False
        
    def move(self, steps: int) -> bool:
        """Move the player by the given number of steps.
        
        Args:
            steps: Number of steps to move (1-6)
            
        Returns:
            bool: True if the player has won (reached or passed 100), False otherwise
        """
        if self.position + steps <= 100:
            self.position += steps
            return self.position == 100
        return False
    
    def set_position(self, position: int) -> None:
        """Set the player's position directly.
        
        Args:
            position: The new position (1-100)
        """
        self.position = max(0, min(100, position))
    
    def get_cell_center(self, board_size: int, cell_size: int, window_height: int) -> Tuple[int, int]:
        """Calculate the center position of the player's current cell.
        
        Args:
            board_size: Number of cells per row/column
            cell_size: Size of each cell in pixels
            window_height: Height of the game window
            
        Returns:
            Tuple[int, int]: (x, y) coordinates of the cell center
        """
        if self.position < 1 or self.position > 100:
            return (0, 0)
            
        # Calculate row and column (0-based)
        row = (self.position - 1) // board_size
        col = (self.position - 1) % board_size
        
        # Handle snake pattern (alternate direction each row)
        if row % 2 == 1:
            col = (board_size - 1) - col
        
        # Calculate center coordinates
        x = col * cell_size + cell_size // 2
        y = window_height - (row * cell_size) - cell_size // 2
        
        return (x, y)
