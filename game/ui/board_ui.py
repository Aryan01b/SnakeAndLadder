"""Board rendering for the Snake and Ladder game."""

import pygame
from typing import List, Tuple, Optional
from ..models.player import Player
from ..models.board import Board
from .. import constants as const

class BoardUI:
    """Handles rendering of the game board."""
    
    def __init__(self, board: Board, players: List[Player]):
        """Initialize the board UI.
        
        Args:
            board: The game board
            players: List of players
        """
        self.board = board
        self.players = players
        self.cell_size = const.CELL_SIZE
        self.window_height = const.WINDOW_SIZE[1]
        
        # Initialize fonts
        self.font = pygame.font.SysFont('Arial', 16)
        self.large_font = pygame.font.SysFont('Arial', 24, bold=True)
    
    def draw(self, surface: pygame.Surface) -> None:
        """Draw the game board.
        
        Args:
            surface: The pygame surface to draw on
        """
        self._draw_grid(surface)
        self._draw_snakes_and_ladders(surface)
        self._draw_players(surface)
    
    def _draw_grid(self, surface: pygame.Surface) -> None:
        """Draw the game board grid."""
        for row in range(self.board.size):
            for col in range(self.board.size):
                # Calculate position (board is on the left side)
                x = col * self.cell_size
                y = self.window_height - (row * self.cell_size) - self.cell_size
                
                # Alternate cell colors
                cell_color = const.YELLOW if (row + col) % 2 == 0 else const.WHITE
                pygame.draw.rect(surface, cell_color, (x, y, self.cell_size, self.cell_size))
                
                # Draw cell border
                pygame.draw.rect(surface, const.BLACK, (x, y, self.cell_size, self.cell_size), 1)
                
                # Draw cell number
                self._draw_cell_number(surface, row, col, x, y)
    
    def _draw_cell_number(self, surface: pygame.Surface, row: int, col: int, x: int, y: int) -> None:
        """Draw the number in a cell."""
        # Calculate cell number based on snake pattern
        if row % 2 == 0:
            number = row * self.board.size + col + 1
        else:
            number = (row + 1) * self.board.size - col
        
        # Draw the number
        text = self.font.render(str(number), True, const.BLACK)
        text_rect = text.get_rect(center=(x + self.cell_size//2, y + self.cell_size//2))
        surface.blit(text, text_rect)
    
    def _draw_snakes_and_ladders(self, surface: pygame.Surface) -> None:
        """Draw snakes and ladders on the board."""
        # Draw ladders first (so they appear below snakes)
        for start, end in self.board.ladders.items():
            self._draw_ladder(surface, start, end)
        
        # Draw snakes
        for start, end in self.board.snakes.items():
            self._draw_snake(surface, start, end)
    
    def _draw_ladder(self, surface: pygame.Surface, start: int, end: int) -> None:
        """Draw a ladder on the board."""
        # Get start and end positions
        start_pos = self._get_cell_center(start)
        end_pos = self._get_cell_center(end)
        
        # Draw ladder with two side rails and rungs
        ladder_color = (139, 69, 19)  # Brown
        rail_width = 5
        
        # Draw side rails
        offset = 10
        pygame.draw.line(
            surface, ladder_color,
            (start_pos[0] - offset, start_pos[1]),
            (end_pos[0] - offset, end_pos[1]),
            rail_width
        )
        pygame.draw.line(
            surface, ladder_color,
            (start_pos[0] + offset, start_pos[1]),
            (end_pos[0] + offset, end_pos[1]),
            rail_width
        )
        
        # Draw rungs
        rung_count = 5
        for i in range(1, rung_count):
            progress = i / rung_count
            x1 = start_pos[0] + (end_pos[0] - start_pos[0]) * progress
            y1 = start_pos[1] + (end_pos[1] - start_pos[1]) * progress
            x2 = x1 - 2 * offset * (1 if start_pos[0] < end_pos[0] else -1)
            y2 = y1
            
            pygame.draw.line(
                surface, ladder_color,
                (x1, y1), (x2, y2),
                3
            )
    
    def _draw_snake(self, surface: pygame.Surface, start: int, end: int) -> None:
        """Draw a snake on the board."""
        # Get start and end positions
        start_pos = self._get_cell_center(start)
        end_pos = self._get_cell_center(end)
        
        # Draw snake body with a curved line
        control_x = (start_pos[0] + end_pos[0]) // 2 + 30
        control_y = (start_pos[1] + end_pos[1]) // 2 - 40
        
        # Draw snake body as a curve
        points = [start_pos]
        steps = 10
        for i in range(1, steps):
            t = i / steps
            # Quadratic bezier curve for smooth snake body
            x = (1-t)**2 * start_pos[0] + 2*(1-t)*t*control_x + t**2*end_pos[0]
            y = (1-t)**2 * start_pos[1] + 2*(1-t)*t*control_y + t**2*end_pos[1]
            points.append((x, y))
        points.append(end_pos)
        
        # Draw snake body
        if len(points) > 1:
            pygame.draw.lines(surface, const.GREEN, False, points, 10)
        
        # Draw snake head
        pygame.draw.circle(surface, const.GREEN, start_pos, 8)
        
        # Draw eyes on the head
        direction = 1 if start_pos[0] < end_pos[0] else -1
        pygame.draw.circle(
            surface, const.WHITE,
            (int(start_pos[0] + 3 * direction), int(start_pos[1] - 3)),
            3
        )
    
    def _draw_players(self, surface: pygame.Surface) -> None:
        """Draw all players on the board."""
        for i, player in enumerate(self.players):
            if 1 <= player.position <= 100:
                x, y = player.get_cell_center(
                    self.board.size,
                    self.cell_size,
                    self.window_height
                )
                
                # Offset players so they don't overlap
                offset = (i - (len(self.players) - 1) / 2) * 20
                x += offset
                
                # Draw player token
                pygame.draw.circle(surface, player.color, (int(x), int(y)), const.PLAYER_RADIUS)
                
                # Draw player name
                name_surface = self.font.render(player.name[0], True, const.WHITE)
                name_rect = name_surface.get_rect(center=(x, y))
                surface.blit(name_surface, name_rect)
    
    def _get_cell_center(self, position: int) -> Tuple[int, int]:
        """Get the center coordinates of a cell."""
        return self.board.get_cell_coordinates(
            position,
            self.cell_size,
            self.window_height
        )
