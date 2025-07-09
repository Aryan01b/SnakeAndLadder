"""Sidebar UI for the Snake and Ladder game."""

import pygame
from typing import List, Tuple, Optional, Dict, Any
from ..models.player import Player
from .. import constants as const

class SidebarUI:
    """Handles rendering of the game sidebar."""
    
    def __init__(self, width: int, height: int):
        """Initialize the sidebar UI.
        
        Args:
            width: Width of the sidebar
            height: Height of the sidebar (should match window height)
        """
        self.width = width
        self.height = height
        self.padding = 20
        
        # Initialize fonts
        self.title_font = pygame.font.SysFont('Arial', 28, bold=True)
        self.header_font = pygame.font.SysFont('Arial', 24, bold=True)
        self.font = pygame.font.SysFont('Arial', 18)
        self.small_font = pygame.font.SysFont('Arial', 16)
    
    def draw(self, surface: pygame.Surface, current_player: Player, dice_value: int, 
             game_over: bool = False, winner: Optional[Player] = None) -> None:
        """Draw the sidebar.
        
        Args:
            surface: The pygame surface to draw on
            current_player: The current player
            dice_value: Current dice value to display
            game_over: Whether the game is over
            winner: The winning player (if game is over)
        """
        # Draw background
        self._draw_background(surface)
        
        # Draw title
        self._draw_title(surface)
        
        # Draw current player info
        self._draw_player_info(surface, current_player)
        
        # Draw dice
        self._draw_dice(surface, dice_value)
        
        # Draw game over message if needed
        if game_over and winner:
            self._draw_game_over(surface, winner)
        
        # Draw instructions
        self._draw_instructions(surface)
    
    def _draw_background(self, surface: pygame.Surface) -> None:
        """Draw the sidebar background."""
        # Draw background (positioned on the right side)
        x = const.SIDEBAR_X
        pygame.draw.rect(surface, const.LIGHT_GRAY, (x, 0, self.width, self.height))
        
        # Draw separator line
        pygame.draw.line(surface, const.GRAY, (x, 0), (x, self.height), 2)
    
    def _draw_title(self, surface: pygame.Surface) -> None:
        """Draw the game title."""
        # Draw title (positioned in the sidebar)
        x = const.SIDEBAR_X
        title = self.title_font.render("Snake & Ladder", True, const.BLACK)
        title_rect = title.get_rect(center=(x + self.width // 2, 40))
        surface.blit(title, title_rect)
    
    def _draw_player_info(self, surface: pygame.Surface, player: Player) -> None:
        """Draw information about the current player."""
        # Draw section header
        header = self.header_font.render("Current Turn", True, const.BLACK)
        surface.blit(header, (const.SIDEBAR_X + self.padding, 80))
        
        # Draw player info
        x = const.SIDEBAR_X
        player_text = f"{player.name}'s Turn"
        text_surface = self.font.render(player_text, True, player.color)
        text_rect = text_surface.get_rect(center=(x + self.width // 2, 120))
        surface.blit(text_surface, text_rect)
    
    def _draw_dice(self, surface: pygame.Surface, value: int) -> None:
        """Draw the dice."""
        # Draw section header
        header = self.header_font.render("Dice", True, const.BLACK)
        surface.blit(header, (const.SIDEBAR_X + self.padding, 160))
        
        # Draw dice background (centered in the sidebar)
        x = const.SIDEBAR_X
        dice_size = 100
        dice_x = x + (self.width - dice_size) // 2
        dice_y = 200
        
        # Draw shadow
        pygame.draw.rect(
            surface, (200, 200, 200, 100),
            (dice_x + 5, dice_y + 5, dice_size, dice_size),
            border_radius=10
        )
        
        # Draw dice
        pygame.draw.rect(
            surface, const.WHITE,
            (dice_x, dice_y, dice_size, dice_size),
            border_radius=10
        )
        
        # Draw border
        pygame.draw.rect(
            surface, const.BLACK,
            (dice_x, dice_y, dice_size, dice_size),
            width=2, border_radius=10
        )
        
        # Draw dots
        self._draw_dice_dots(surface, value, dice_x, dice_y, dice_size)
    
    def _draw_dice_dots(self, surface: pygame.Surface, value: int, x: int, y: int, size: int) -> None:
        """Draw the dots on the dice."""
        dot_radius = size // 12
        center_x = x + size // 2
        center_y = y + size // 2
        offset = size // 4
        
        # Dot positions for each dice value (1-6)
        dot_config = {
            1: [(center_x, center_y)],
            2: [
                (center_x - offset, center_y - offset),
                (center_x + offset, center_y + offset)
            ],
            3: [
                (center_x - offset, center_y - offset),
                (center_x, center_y),
                (center_x + offset, center_y + offset)
            ],
            4: [
                (center_x - offset, center_y - offset),
                (center_x + offset, center_y - offset),
                (center_x - offset, center_y + offset),
                (center_x + offset, center_y + offset)
            ],
            5: [
                (center_x - offset, center_y - offset),
                (center_x + offset, center_y - offset),
                (center_x, center_y),
                (center_x - offset, center_y + offset),
                (center_x + offset, center_y + offset)
            ],
            6: [
                (center_x - offset, center_y - offset),
                (center_x - offset, center_y),
                (center_x - offset, center_y + offset),
                (center_x + offset, center_y - offset),
                (center_x + offset, center_y),
                (center_x + offset, center_y + offset)
            ]
        }
        
        # Draw the dots
        for pos in dot_config.get(value, []):
            pygame.draw.circle(surface, const.BLACK, pos, dot_radius)
    
    def _draw_game_over(self, surface: pygame.Surface, winner: Player) -> None:
        """Draw the game over message."""
        # Create semi-transparent overlay
        overlay = pygame.Surface((const.BOARD_WIDTH, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        surface.blit(overlay, (0, 0))
        
        # Draw game over text
        game_over_text = self.header_font.render("GAME OVER", True, const.WHITE)
        winner_text = self.font.render(f"{winner.name} wins!", True, const.WHITE)
        restart_text = self.small_font.render("Press R to restart", True, const.WHITE)
        
        # Center the text
        center_x = self.width // 2
        center_y = self.height // 2
        
        surface.blit(game_over_text, 
                    (const.SIDEBAR_X + center_x - game_over_text.get_width() // 2, center_y - 60))
        surface.blit(winner_text, 
                    (const.SIDEBAR_X + center_x - winner_text.get_width() // 2, center_y))
        surface.blit(restart_text, 
                    (const.SIDEBAR_X + center_x - restart_text.get_width() // 2, center_y + 60))
    
    def _draw_instructions(self, surface: pygame.Surface) -> None:
        """Draw game instructions."""
        # Draw section header
        x = const.SIDEBAR_X
        header = self.header_font.render("How to Play", True, const.BLACK)
        surface.blit(header, (x + self.padding, 340))
        
        # Draw instructions
        instructions = [
            "• Click the dice to roll",
            "• Land on ladders to climb up",
            "• Avoid snakes or slide down",
            "• First to reach 100 wins!",
            "",
            "Controls:",
            "SPACE: Roll dice",
            "R: Restart game",
            "Q/ESC: Quit"
        ]
        
        y_offset = 380
        line_height = 24
        
        for i, line in enumerate(instructions):
            if line.endswith(':'):
                # Header line
                text = self.font.render(line, True, const.BLACK)
                surface.blit(text, (const.SIDEBAR_X + self.padding, y_offset + i * line_height))
            else:
                # Regular line
                x = const.SIDEBAR_X
                text = self.small_font.render(line, True, const.DARK_GRAY)
                surface.blit(text, (x + self.padding + 10, y_offset + i * line_height))
