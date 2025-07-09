import random
import time
import os
import sys
from enum import Enum
from typing import List, Tuple, Dict, Optional
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import track
from rich.text import Text
from rich import box
from rich.layout import Layout
from rich.align import Align
from rich.live import Live
from rich.prompt import IntPrompt, Prompt, Confirm
from rich.style import Style

# Initialize rich console
console = Console()

class GameState(Enum):
    MAIN_MENU = 1
    PLAYING = 2
    GAME_OVER = 3

# Game constants
BOARD_SIZE = 10
DICE_FACES = 6
MAX_POS = BOARD_SIZE * BOARD_SIZE
PAUSE = 0.8

# Colors
COLORS = [
    "red", "blue", "green", "yellow",
    "magenta", "cyan", "bright_red", "bright_blue"
]

# Snake and Ladder positions (start: end)
snakes = {
    17: 7, 54: 34, 62: 19, 64: 60,
    87: 24, 93: 73, 96: 75, 98: 79
}

ladders = {
    3: 37, 5: 14, 9: 31, 21: 42,
    28: 84, 51: 67, 71: 90, 80: 99
}

# Game symbols
SNAKE_HEAD = "🐍"
SNAKE_TAIL = "🐉"
LADDER_BOTTOM = "🪜"
LADDER_TOP = "🏁"
DICE = "🎲"
TROPHY = "🏆"
PLAYER = "😊"

def clear_screen():
    """Clear the terminal screen."""
    console.clear()

def generate_board(players: List[Tuple[str, int]]) -> Table:
    """Generate a rich table for the game board."""
    # Create a table for the board
    board = Table(show_header=False, show_lines=True, box=box.ROUNDED, padding=0)
    
    # Add columns (we'll add 10 columns for a 10x10 grid)
    for _ in range(BOARD_SIZE):
        board.add_column(justify="center", width=6)
    
    # Create a mapping of positions to player numbers
    pos_to_players = {}
    for idx, (_, pos) in enumerate(players):
        if pos not in pos_to_players:
            pos_to_players[pos] = []
        pos_to_players[pos].append(idx + 1)
    
    # Fill the board
    for row in range(BOARD_SIZE, 0, -1):
        row_cells = []
        
        # Determine if we're moving left or right
        if row % 2 == 0:
            cols = range(BOARD_SIZE, 0, -1)  # Right to left for even rows
        else:
            cols = range(1, BOARD_SIZE + 1)  # Left to right for odd rows
        
        for col in cols:
            pos = (row - 1) * BOARD_SIZE + col
            cell_content = Text()
            
            # Add position number
            cell_content.append(f"{pos:3}\n", style="dim")
            
            # Add players in this position
            if pos in pos_to_players:
                players_here = pos_to_players[pos]
                for p_num in players_here:
                    color = COLORS[(p_num - 1) % len(COLORS)]
                    cell_content.append(f" {PLAYER}", style=f"bold {color}")
                cell_content.append(" ")
            
            # Add snakes and ladders
            if pos in snakes:
                cell_content.append(f" {SNAKE_HEAD}", style="red")
            elif pos in ladders:
                if pos < ladders[pos]:  # Bottom of ladder
                    cell_content.append(f" {LADDER_BOTTOM}", style="green")
                else:  # Top of ladder (shouldn't happen with current data)
                    cell_content.append(f" {LADDER_TOP}", style="green")
            
            # Add snakes' tails and ladders' tops
            if pos in snakes.values():
                cell_content.append(f" {SNAKE_TAIL}", style="red")
            if pos in ladders.values():
                cell_content.append(f" {LADDER_TOP}", style="green")
            
            row_cells.append(cell_content)
        
        board.add_row(*row_cells)
    
    return board

def display_game_state(players: List[Tuple[str, int]], current_player: int, last_roll: int = None):
    """Display the current game state with rich formatting."""
    layout = Layout()
    
    # Split the layout into header, board, and status sections
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="board", ratio=2),
        Layout(name="status", size=8)
    )
    
    # Header
    header = Table.grid(expand=True)
    header.add_column(justify="center")
    header.add_row(
        Panel.fit(
            "🐍 [bold]SNAKE[/] [bold green]&[/] [bold blue]LADDER[/] 🪜",
            style="bold blue",
            border_style="bright_blue"
        )
    )
    layout["header"].update(header)
    
    # Board
    board = generate_board(players)
    layout["board"].update(Panel(board, title="Game Board", border_style="green"))
    
    # Status
    status = Table.grid(expand=True)
    status.add_column()
    
    # Current player info
    current_name, current_pos = players[current_player]
    status.add_row(
        Panel(
            f"🎮 [bold]{current_name}'s[/] turn\n"
            f"📍 Position: [bold]{current_pos}[/]/100\n"
            f"🎲 Last roll: [bold]{last_roll if last_roll is not None else '--'}",
            title="Current Turn",
            border_style=COLORS[current_player % len(COLORS)]
        )
    )
    
    # Players' status
    players_table = Table(show_header=True, box=box.ROUNDED)
    players_table.add_column("Player", style="bold")
    players_table.add_column("Position")
    players_table.add_column("Status")
    
    for i, (name, pos) in enumerate(players):
        status_text = ""
        if pos == MAX_POS:
            status_text = f"[green]Winner! {TROPHY}[/]"
        elif i == current_player:
            status_text = "[yellow]Rolling...[/]"
        
        players_table.add_row(
            f"[bold {COLORS[i % len(COLORS)]}]{name}[/]",
            str(pos),
            status_text
        )
    
    status.add_row("")
    status.add_row(Panel(players_table, title="Players", border_style="dim"))
    
    # Instructions
    instructions = (
        "[dim]Press [bold]Enter[/] to roll the dice\n"
        "Press [bold]Q[/] to quit[/]"
    )
    status.add_row("")
    status.add_row(Panel(instructions, border_style="dim"))
    
    layout["status"].update(status)
    
    # Display everything
    console.print(layout)

def show_game_over(winner: str):
    """Display the game over screen."""
    console.clear()
    console.print("\n" * 3, style="white")
    
    # Create a panel for the winner
    winner_panel = Panel.fit(
        f"\n{TROPHY * 3} [bold green]CONGRATULATIONS![/] {TROPHY * 3}\n\n"
        f"[bold yellow]{winner}[/] [white]wins the game![/]\n\n"
        f"[dim]Press any key to continue...[/]",
        width=60,
        style="on blue",
        border_style="yellow"
    )
    
    console.print(Panel(winner_panel, box=box.DOUBLE_EDGE, style="on bright_black"))
    input()

def roll_dice() -> int:
    """Simulate rolling a die with a rich animation."""
    with console.status("🎲 Rolling the die...", spinner="dots"):
        time.sleep(0.8)
        result = random.randint(1, DICE_FACES)
        
        # Create a visual dice face
        dice_faces = {
            1: "[ ]\n ● \n[ ]",
            2: "●  \n   \n  ●",
            3: "●  \n ● \n  ●",
            4: "● ●\n   \n● ●",
            5: "● ●\n ● \n● ●",
            6: "● ●\n● ●\n● ●"
        }
        
        # Show the dice face
        dice_panel = Panel(
            f"\n{dice_faces[result]}\n",
            title=f"{DICE} Rolled: {result}",
            border_style="yellow"
        )
        console.print(dice_panel)
        time.sleep(0.5)
        
        return result

def move_player(player_idx: int, current_pos: int, steps: int, players: List[Tuple[str, int]]) -> int:
    """Move a player and handle snakes and ladders with rich output."""
    name, pos = players[player_idx]
    new_pos = pos + steps
    
    if new_pos > MAX_POS:
        console.print(
            f"[yellow]You need exactly {MAX_POS - pos} to win![/] :cross_mark:",
            style="bold yellow"
        )
        time.sleep(1)
        return pos
    
    # Animate the movement
    console.print(f"[cyan]{name} moves from {pos} to {new_pos}[/] :arrow_forward:")
    
    # Check for snakes and ladders
    if new_pos in snakes:
        final_pos = snakes[new_pos]
        console.rule(f"[red]SNAKE BITE![/] {name} slides down to {final_pos} {SNAKE_HEAD}", 
                    style="red", align="center")
        new_pos = final_pos
        time.sleep(1)
    elif new_pos in ladders:
        final_pos = ladders[new_pos]
        console.rule(f"[green]LADDER![/] {name} climbs up to {final_pos} {LADDER_TOP}", 
                    style="green", align="center")
        new_pos = final_pos
        time.sleep(1)
    
    # Update player position
    players[player_idx] = (name, new_pos)
    return new_pos

def play_game(num_players: int = 2):
    """Main game loop with rich interface."""
    # Get player names
    players = []
    console.clear()
    console.rule("👥 Player Setup", style="bold blue")
    
    for i in range(num_players):
        while True:
            name = Prompt.ask(
                f"[bold {COLORS[i % len(COLORS)]}]Enter Player {i+1}'s name[/]"
            ).strip()
            if name:
                players.append((name, 1))  # (name, position)
                break
    
    current_player = 0
    last_roll = None
    
    with console.screen() as screen:
        while True:
            name, pos = players[current_player]
            
            # Display game state
            display_game_state(players, current_player, last_roll)
            
            # Get input with timeout for animation
            key = input("Press Enter to roll (Q to quit): ").strip().lower()
            if key == 'q':
                if Confirm.ask("Are you sure you want to quit?"):
                    console.print("\nThanks for playing!")
                    return
                continue
            
            # Roll the dice
            last_roll = roll_dice()
            new_pos = move_player(current_player, pos, last_roll, players)
            
            # Check for win
            if new_pos == MAX_POS:
                show_game_over(name)
                break
            
            # Next player's turn
            current_player = (current_player + 1) % num_players
            
            # Small delay for smooth transition
            time.sleep(0.5)

def show_main_menu() -> bool:
    """Display the main menu and return whether to start the game."""
    console.clear()
    console.print("\n" * 2, style="white")
    
    # Create a fancy title
    title = """
    ╔══════════════════════════════════════════════╗
    ║    🐍 [bold green]SNAKE[/] [bold yellow]&[/] [bold blue]LADDER[/] 🪜    ║
    ╚══════════════════════════════════════════════╝
    """
    
    console.print(Panel(title.strip(), border_style="blue"))
    console.print("\n")
    
    # Game options
    options = [
        ("1", "Start New Game"),
        ("2", "How to Play"),
        ("Q", "Quit")
    ]
    
    # Display options in a table
    menu = Table(show_header=False, box=box.ROUNDED, expand=True)
    menu.add_column("Option", justify="center", style="bold yellow")
    menu.add_column("Description", justify="left")
    
    for opt, desc in options:
        menu.add_row(f"[bold]{opt}[/]", desc)
    
    console.print(Panel(menu, title="Main Menu", border_style="blue"))
    
    # Get user choice
    while True:
        choice = Prompt.ask("\nSelect an option", choices=["1", "2", "q"], show_choices=False).lower()
        
        if choice == "1":
            return True
        elif choice == "2":
            show_how_to_play()
            return show_main_menu()
        else:
            return False

def show_how_to_play():
    """Display the how to play instructions."""
    console.clear()
    console.print("\n" * 2, style="white")
    
    instructions = """
    [bold underline]HOW TO PLAY[/bold underline]\n\n
    [bold]Objective:[/] Be the first player to reach the 100th square.\n\n
    [bold]Gameplay:[/]
    • Each player takes turns rolling the dice and moving forward.\n
    • If you land on the bottom of a ladder, you climb up to the top.\n      [green]Ladders:[/] 3→37, 5→14, 9→31, 21→42, 28→84, 51→67, 71→90, 80→99\n
    • If you land on a snake's head, you slide down to its tail.\n      [red]Snakes:[/] 17→7, 54→34, 62→19, 64→60, 87→24, 93→73, 96→75, 98→79\n
    • You must roll the exact number needed to reach 100.\n    """
    
    console.print(Panel(
        instructions.strip(),
        title="How to Play",
        border_style="green",
        padding=(1, 2)
    ))
    
    input("\nPress Enter to return to the main menu...")

def start_game():
    """Initialize and start the game with rich interface."""
    try:
        while True:
            if not show_main_menu():
                console.print("\n[bold]Thanks for playing! Goodbye! 👋[/]\n")
                break
            
            # Get number of players
            console.clear()
            console.rule("👥 Number of Players", style="bold blue")
            
            num_players = IntPrompt.ask(
                "Enter number of players",
                default=2,
                show_default=True,
                choices=["2", "3", "4"]
            )
            
            # Start the game
            play_game(num_players)
            
            # Ask to play again
            if not Confirm.ask("\nWould you like to play again?"):
                console.print("\n[bold]Thanks for playing! Goodbye! 👋[/]\n")
                break
                
    except KeyboardInterrupt:
        console.print("\n\n[bold]Game ended by user. Thanks for playing![/]")
    except Exception as e:
        console.print(f"\n[bold red]An error occurred:[/] {e}")
        console.print("\nPlease make sure you have installed all required packages:")
        console.print("pip install rich colorama")
        sys.exit(1)

if __name__ == "__main__":
    start_game()