# Snake and Ladder
# By Aryan Arlikar

import random2
import time
import sys

DICE_FACE=6
MAX_POS=100
PAUSE=1

snake_len={
    17:7,
    54:34,
    62:19,
    64:60,
    87:24,
    93:73,
    96:75,
    98:79
}

ladder_step={
    3:37,
    5:14,
    9:31,
    21:42,
    28:84,
    51:67,
    71:90,
    80:99
}

def start_msg():
    msg = """
    Welcome to Snake and Ladder Game.

    Rules:
      1. Initally both the players are at starting position i.e. 0. 
      2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
      3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
      4. The first player to get to the FINAL position is the winner.
      5. Hit enter to roll the dice.
      6. Press "q" for exiting the game
    """
    print(msg)

def get_player_name():
    player1=None
    while not player1:
        player1=input("Enter Player1's Name:").strip().capitalize()
    player2=None
    while not player2:
        player2=input("Enter Player2's Name:").strip().capitalize()
    print(f"The Match is Between {player1} and {player2}")
    return player1,player2

def dice_face_no(player_name):
    time.sleep(PAUSE)
    face_no=random2.randint(1,DICE_FACE)
    print(f"{player_name} got a {face_no}")
    return face_no

def snake_n_ladder(player_name, current_value, dice_no):
    time.sleep(PAUSE)
    old_value=current_value
    current_value+=dice_no
    
    if current_value>MAX_POS:
        print(f"\nYou need {MAX_POS-old_value} to win...")
        return old_value
    print(f"Player {player_name} moved from {old_value} to {current_value}!")
    if current_value in snake_len:
        final_value=snake_len.get(current_value)
        print(f"\nSnake bite player {player_name}!!\n/\/\/\/\/\/\/>>\nGo down from {current_value} to {final_value}")
    elif current_value in ladder_step:
        final_value=ladder_step.get(current_value)
        print(f"\nPlayer {player_name} is steping up the ladder!!\n##########\nMove from {current_value} to {final_value}")
    else:
        final_value=current_value
    return final_value

def is_win(player_name,current_position):
    time.sleep(PAUSE)
    if MAX_POS==current_position:
        print(f"\n\tPlayer {player_name} Won!!!")
        print("Congratulations!!!", player_name)
        sys.exit(1)

def start_game():
    start_msg()
    time.sleep(PAUSE)
    p1,p2=get_player_name()
    time.sleep(PAUSE)
    
    p1_current_position=0
    p2_current_position=0
    
    while True:
        time.sleep(PAUSE)
        p1_input=input(f"\n{p1}: Press Enter to Roll dice...\n Or 'q' for Exit...")
        if p1_input=='q':
            sys.exit(1)
        print("Rolling dice...")
        dice_value=dice_face_no(p1)
        time.sleep(PAUSE)
        p1_current_position=snake_n_ladder(p1,p1_current_position,dice_value)
        is_win(p1,p1_current_position)
        
        time.sleep(PAUSE)
        p2_input=input(f"\n{p2}: Press Enter to Roll dice...\n Or 'q' for Exit...")
        if p2_input=='q':
            sys.exit(1)
        print("Rolling dice...")
        dice_value=dice_face_no(p2)
        time.sleep(PAUSE)
        p2_current_position=snake_n_ladder(p2,p2_current_position,dice_value)
        is_win(p2,p2_current_position)
    
if __name__=='__main__':
    start_game()