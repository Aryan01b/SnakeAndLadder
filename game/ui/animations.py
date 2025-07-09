"""Animation system for the Snake and Ladder game."""

import pygame
import math
from typing import List, Dict, Any, Optional, Callable, Tuple
from ..models.player import Player

class Animation:
    """Base class for animations."""
    
    def __init__(self, duration: float, on_complete: Optional[Callable] = None):
        """Initialize the animation.
        
        Args:
            duration: Duration of the animation in seconds
            on_complete: Optional callback when animation completes
        """
        self.duration = duration * 1000  # Convert to milliseconds
        self.start_time = pygame.time.get_ticks()
        self.is_complete = False
        self.on_complete = on_complete
    
    def update(self) -> bool:
        """Update the animation.
        
        Returns:
            bool: True if the animation is complete, False otherwise
        """
        if self.is_complete:
            return True
            
        elapsed = pygame.time.get_ticks() - self.start_time
        progress = min(elapsed / self.duration, 1.0)
        
        self._update_animation(progress)
        
        if progress >= 1.0:
            self.is_complete = True
            if self.on_complete:
                self.on_complete()
            return True
        return False
    
    def _update_animation(self, progress: float) -> None:
        """Update the animation state based on progress (0.0 to 1.0).
        
        Args:
            progress: Animation progress from 0.0 to 1.0
        """
        raise NotImplementedError("Subclasses must implement _update_animation")


class MoveAnimation(Animation):
    """Animation for moving a player between cells."""
    
    def __init__(self, player: Player, target_position: int, duration: float, 
                 board_size: int, cell_size: int, window_height: int,
                 on_complete: Optional[Callable] = None):
        """Initialize the move animation.
        
        Args:
            player: The player to animate
            target_position: The target position on the board
            duration: Duration of the animation in seconds
            board_size: Size of the game board
            cell_size: Size of each cell in pixels
            window_height: Height of the game window
            on_complete: Optional callback when animation completes
        """
        super().__init__(duration, on_complete)
        self.player = player
        self.start_pos = player.get_cell_center(board_size, cell_size, window_height)
        self.target_pos = self._calculate_target_position(
            target_position, board_size, cell_size, window_height)
        
        # Store original position to reset if needed
        self.original_position = player.position
        
    def _calculate_target_position(self, position: int, board_size: int, 
                                 cell_size: int, window_height: int) -> Tuple[float, float]:
        """Calculate the target position in screen coordinates."""
        row = (position - 1) // board_size
        col = (position - 1) % board_size
        
        # Handle snake pattern (alternate direction each row)
        if row % 2 == 1:
            col = (board_size - 1) - col
        
        x = col * cell_size + cell_size // 2
        y = window_height - (row * cell_size) - cell_size // 2
        
        return (x, y)
    
    def _update_animation(self, progress: float) -> None:
        """Update the player's position based on animation progress."""
        # Use smooth step for easing
        t = self._ease_in_out_cubic(progress)
        
        # Interpolate between start and target positions
        x = self.start_pos[0] + (self.target_pos[0] - self.start_pos[0]) * t
        y = self.start_pos[1] + (self.target_pos[1] - self.start_pos[1]) * t
        
        # Update player's visual position (not logical position)
        self.player.rect.center = (x, y)
    
    def _ease_in_out_cubic(self, t: float) -> float:
        """Easing function for smooth start and end."""
        t *= 2
        if t < 1:
            return 0.5 * t * t * t
        t -= 2
        return 0.5 * (t * t * t + 2)


class DiceRollAnimation(Animation):
    """Animation for rolling the dice."""
    
    def __init__(self, duration: float, on_update: Callable[[int], None], 
                 on_complete: Optional[Callable] = None):
        """Initialize the dice roll animation.
        
        Args:
            duration: Duration of the animation in seconds
            on_update: Callback called with the current dice value
            on_complete: Optional callback when animation completes
        """
        super().__init__(duration, on_complete)
        self.on_update = on_update
        self.last_value = 0
    
    def _update_animation(self, progress: float) -> None:
        """Update the dice roll animation."""
        # Generate random dice values during the animation
        value = pygame.time.get_ticks() % 6 + 1
        if value != self.last_value:
            self.last_value = value
            self.on_update(value)


class AnimationManager:
    """Manages animations for the game."""
    
    def __init__(self):
        """Initialize the animation manager."""
        self.animations: List[Animation] = []
    
    def add_animation(self, animation: Animation) -> None:
        """Add an animation to be managed.
        
        Args:
            animation: The animation to add
        """
        self.animations.append(animation)
    
    def update(self) -> None:
        """Update all active animations and remove completed ones."""
        # Update animations in reverse order so we can remove completed ones
        for i in range(len(self.animations) - 1, -1, -1):
            if self.animations[i].update():
                self.animations.pop(i)
    
    def is_animating(self) -> bool:
        """Check if any animations are currently playing.
        
        Returns:
            bool: True if animations are in progress, False otherwise
        """
        return len(self.animations) > 0
    
    def clear(self) -> None:
        """Clear all animations."""
        self.animations.clear()
