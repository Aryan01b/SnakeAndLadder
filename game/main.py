"""Main game module for the Snake and Ladder game."""

import sys
import pygame
from typing import List, Optional, Dict, Any, Callable, Tuple

from .models.player import Player
from .models.board import Board
from .core.game_logic import GameLogic
from .ui.board_ui import BoardUI
from .ui.sidebar_ui import SidebarUI
from .ui.animations import AnimationManager, MoveAnimation, DiceRollAnimation
from . import constants as const

class SnakeAndLadderGame:
    """Main game class for the Snake and Ladder game."""
    
    def __init__(self):
        """Initialize the game."""
        # Initialize Pygame
        pygame.init()
        
        # Create game window
        self.screen = pygame.display.set_mode(const.WINDOW_SIZE)
        pygame.display.set_caption("Snake and Ladder")
        
        # Initialize clock for controlling frame rate
        self.clock = pygame.time.Clock()
        
        # Create game objects
        self.players = [
            Player("Player 1", const.RED),
            Player("Player 2", const.BLUE)
        ]
        
        self.board = Board(const.SNAKES, const.LADDERS, const.BOARD_SIZE)
        self.game_logic = GameLogic(self.players, self.board)
        
        # Initialize UI components
        self.board_ui = BoardUI(self.board, self.players)
        self.sidebar_ui = SidebarUI(const.SIDEBAR_WIDTH, const.WINDOW_SIZE[1])
        
        # Initialize animation manager
        self.animation_manager = AnimationManager()
        
        # Game state
        self.running = True
        self.show_game_over = False
    
    def run(self) -> None:
        """Run the main game loop."""
        while self.running:
            self._handle_events()
            self._update()
            self._render()
            self.clock.tick(const.FPS)
        
        # Clean up
        pygame.quit()
        sys.exit()
    
    def _handle_events(self) -> None:
        """Handle Pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event.key)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self._handle_click(event.pos)
    
    def _handle_keydown(self, key: int) -> None:
        """Handle key press events."""
        if key == pygame.K_ESCAPE or key == pygame.K_q:
            self.running = False
        
        elif key == pygame.K_r:
            self._reset_game()
        
        elif key == pygame.K_SPACE and not self.animation_manager.is_animating():
            self._roll_dice()
    
    def _handle_click(self, pos: Tuple[int, int]) -> None:
        """Handle mouse click events."""
        # Check if click is on the dice in the sidebar
        dice_rect = pygame.Rect(
            const.SIDEBAR_X + (const.SIDEBAR_WIDTH - 100) // 2,
            200,
            100,
            100
        )
        
        if dice_rect.collidepoint(pos) and not self.animation_manager.is_animating():
            self._roll_dice()
    
    def _roll_dice(self) -> None:
        """Roll the dice and update the game state."""
        if self.game_logic.state.game_over:
            return
        
        # Start dice roll animation
        def on_dice_update(value: int) -> None:
            self.game_logic.state.dice_value = value
        
        def on_dice_complete() -> None:
            # After dice roll completes, process the turn
            success, winner = self.game_logic.play_turn()
            
            if success and winner is None:
                # Animate player movement if needed
                current_player = self.game_logic.state.current_player
                if current_player.position > 0:
                    self._animate_player_move(current_player)
        
        dice_animation = DiceRollAnimation(
            duration=1.0,  # 1 second
            on_update=on_dice_update,
            on_complete=on_dice_complete
        )
        self.animation_manager.add_animation(dice_animation)
    
    def _animate_player_move(self, player: Player) -> None:
        """Animate a player's movement to their new position."""
        def on_move_complete():
            # Check for snakes or ladders after movement
            is_snake, target = self.board.check_snake_or_ladder(player.position)
            if target is not None:
                # Animate snake or ladder movement
                player.set_position(target)
                self._animate_player_move(player)
        
        move_animation = MoveAnimation(
            player=player,
            target_position=player.position,
            duration=0.5,  # 0.5 seconds per move
            board_size=self.board.size,
            cell_size=const.CELL_SIZE,
            window_height=const.WINDOW_SIZE[1],
            on_complete=on_move_complete
        )
        self.animation_manager.add_animation(move_animation)
    
    def _update(self) -> None:
        """Update game state."""
        # Update animations
        self.animation_manager.update()
    
    def _render(self) -> None:
        """Render the game."""
        # Draw the game board
        self.board_ui.draw(self.screen)
        
        # Draw the sidebar
        self.sidebar_ui.draw(
            surface=self.screen,
            current_player=self.game_logic.state.current_player,
            dice_value=self.game_logic.state.dice_value,
            game_over=self.game_logic.state.game_over,
            winner=self.game_logic.state.winner
        )
        
        # Update the display
        pygame.display.flip()
    
    def _reset_game(self) -> None:
        """Reset the game to its initial state."""
        self.game_logic.reset()
        self.animation_manager.clear()
        self.show_game_over = False


def main():
    """Entry point for the game."""
    game = SnakeAndLadderGame()
    game.run()


if __name__ == "__main__":
    main()
