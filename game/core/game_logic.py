"""Core game logic for the Snake and Ladder game."""

import random
from typing import List, Optional, Tuple, Dict, Any
from ..models.player import Player
from ..models.board import Board
from .game_state import GameState

class GameLogic:
    """Handles the core game rules and mechanics."""
    
    def __init__(self, players: List[Player], board: Board):
        """Initialize the game logic.
        
        Args:
            players: List of Player instances
            board: The game board
        """
        self.players = players
        self.board = board
        self.state = GameState(players, board)
    
    def roll_dice(self) -> int:
        """Roll a six-sided die.
        
        Returns:
            int: A random number between 1 and 6
        """
        return random.randint(1, 6)
    
    def move_player(self, player: Player, steps: int) -> Tuple[bool, bool]:
        """Move a player and handle snakes and ladders.
        
        Args:
            player: The player to move
            steps: Number of steps to move (1-6)
            
        Returns:
            Tuple[bool, bool]: 
                - First element: True if the move was valid, False otherwise
                - Second element: True if the player won, False otherwise
        """
        if not (1 <= steps <= 6):
            return False, False
            
        # Move the player
        new_position = player.position + steps
        
        # Check for win condition (exact 100 required)
        if new_position > 100:
            return False, False
            
        player.set_position(new_position)
        
        # Check for win
        if new_position == 100:
            self.state.set_winner(player)
            return True, True
            
        # Check for snakes and ladders
        is_snake, target = self.board.check_snake_or_ladder(new_position)
        if target is not None:
            player.set_position(target)
            
        return True, False
    
    def play_turn(self) -> Tuple[bool, Optional[Player]]:
        """Play a single turn for the current player.
        
        Returns:
            Tuple[bool, Optional[Player]]: 
                - First element: True if the turn was completed successfully
                - Second element: The winning player if the game is over, None otherwise
        """
        if self.state.game_over:
            return False, self.state.winner
            
        player = self.state.current_player
        
        # Roll the dice
        roll = self.roll_dice()
        self.state.last_roll = roll
        self.state.dice_value = roll
        
        # Move the player
        valid_move, has_won = self.move_player(player, roll)
        
        if not valid_move:
            return False, None
            
        # Check for win
        if has_won:
            self.state.set_winner(player)
            return True, player
            
        # Move to next player if not a six
        if roll != 6:
            self.state.next_turn()
            
        return True, None
    
    def reset(self) -> None:
        """Reset the game to its initial state."""
        for player in self.players:
            player.set_position(0)
        self.state = GameState(self.players, self.board)
    
    def get_state(self) -> Dict[str, Any]:
        """Get the current game state as a dictionary."""
        return self.state.to_dict()
    
    def set_state(self, state_data: Dict[str, Any]) -> None:
        """Set the game state from a dictionary."""
        self.state = GameState.from_dict(state_data, self.players, self.board)
