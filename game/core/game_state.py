"""Game state management for the Snake and Ladder game."""

from typing import List, Optional, Dict, Any
from ..models.player import Player
from ..models.board import Board

class GameState:
    """Manages the current state of the game."""
    
    def __init__(self, players: List[Player], board: Board):
        """Initialize the game state.
        
        Args:
            players: List of Player instances
            board: The game board
        """
        self.players = players
        self.board = board
        self.current_player_index = 0
        self.dice_value = 1
        self.game_over = False
        self.winner: Optional[Player] = None
        self.last_roll: Optional[int] = None
        self.message: str = ""
    
    @property
    def current_player(self) -> Player:
        """Get the current player."""
        return self.players[self.current_player_index]
    
    def next_turn(self) -> None:
        """Move to the next player's turn."""
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.last_roll = None
    
    def set_winner(self, player: Player) -> None:
        """Set the winner and end the game.
        
        Args:
            player: The winning player
        """
        self.winner = player
        self.game_over = True
        self.message = f"{player.name} wins!"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the game state to a dictionary for serialization."""
        return {
            'current_player_index': self.current_player_index,
            'dice_value': self.dice_value,
            'game_over': self.game_over,
            'winner': self.winner.name if self.winner else None,
            'last_roll': self.last_roll,
            'message': self.message
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any], players: List[Player], board: Board) -> 'GameState':
        """Create a GameState from a dictionary.
        
        Args:
            data: Dictionary containing game state
            players: List of Player instances
            board: The game board
            
        Returns:
            GameState: A new GameState instance
        """
        state = cls(players, board)
        state.current_player_index = data.get('current_player_index', 0)
        state.dice_value = data.get('dice_value', 1)
        state.game_over = data.get('game_over', False)
        state.last_roll = data.get('last_roll')
        state.message = data.get('message', '')
        
        winner_name = data.get('winner')
        if winner_name:
            state.winner = next((p for p in players if p.name == winner_name), None)
            
        return state
