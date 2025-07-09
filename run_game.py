#!/usr/bin/env python3
"""
Snake and Ladder Game Launcher

This script launches the Snake and Ladder game.
"""

import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import and run the game
from game.main import main

if __name__ == "__main__":
    main()
