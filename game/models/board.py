"""Board model for the Snake and Ladder game."""

from typing import Dict, Tuple, Optional, List

class Board:
    """Represents the game board with snakes and ladders."""
    
    def __init__(self, snakes: Dict[int, int], ladders: Dict[int, int], size: int = 10):
        """Initialize the game board.
        
        Args:
            snakes: Dictionary mapping snake heads to tails {start: end}
            ladders: Dictionary mapping ladder bottoms to tops {start: end}
            size: Size of the board (default: 10x10)
        """
        self.snakes = snakes
        self.ladders = ladders
        self.size = size
        self.total_cells = size * size
    
    def check_snake_or_ladder(self, position: int) -> Tuple[bool, Optional[int]]:
        """Check if a position has a snake or ladder.
        
        Args:
            position: The position to check (1-100)
            
        Returns:
            Tuple[bool, Optional[int]]: 
                - First element: True if snake, False if ladder, None if neither
                - Second element: The target position if snake/ladder, None otherwise
        """
        if position in self.snakes:
            return (True, self.snakes[position])
        elif position in self.ladders:
            return (False, self.ladders[position])
        return (None, None)
    
    def is_valid_position(self, position: int) -> bool:
        """Check if a position is valid on the board.
        
        Args:
            position: The position to check
            
        Returns:
            bool: True if valid (1-100), False otherwise
        """
        return 1 <= position <= self.total_cells
    
    def get_cell_coordinates(self, position: int, cell_size: int, window_height: int) -> Tuple[int, int]:
        """Get the screen coordinates for a board position.
        
        Args:
            position: The board position (1-100)
            cell_size: Size of each cell in pixels
            window_height: Height of the game window
            
        Returns:
            Tuple[int, int]: (x, y) coordinates of the cell's top-left corner
        """
        if not self.is_valid_position(position):
            return (0, 0)
            
        # Convert to 0-based index
        pos = position - 1
        row = pos // self.size
        col = pos % self.size
        
        # Handle snake pattern (alternate direction each row)
        if row % 2 == 1:
            col = (self.size - 1) - col
        
        x = col * cell_size
        y = window_height - ((row + 1) * cell_size)  # y=0 is at top of screen
        
        return (x, y)
    
    def get_position_from_coords(self, x: int, y: int, cell_size: int, window_height: int) -> Optional[int]:
        """Get the board position from screen coordinates.
        
        Args:
            x: X coordinate
            y: Y coordinate
            cell_size: Size of each cell in pixels
            window_height: Height of the game window
            
        Returns:
            Optional[int]: The board position (1-100) or None if invalid
        """
        col = x // cell_size
        row = (window_height - y) // cell_size
        
        if not (0 <= row < self.size and 0 <= col < self.size):
            return None
            
        # Handle snake pattern (alternate direction each row)
        if row % 2 == 1:
            col = (self.size - 1) - col
            
        position = (row * self.size) + col + 1
        
        return position if 1 <= position <= self.total_cells else None
