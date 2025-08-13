# Lets write tic tac toe game code with the help of GitHub Copilot
import random

def greet_players():
    print("=" * 30)
    print(" Welcome to Tic Tac Toe! ")
    print("=" * 30)
    print("Instructions:")
    print(" - Player 1 is 'X' and Player 2 is 'O'.")
    print(" - Players take turns to place their marks on the 3x3 board.")
    print(" - Enter the row and column numbers (0, 1, or 2) to make your move.")
    print(" - The first to get three in a row (horizontally, vertically, or diagonally) wins!")
    print(" - If the board is full and no one wins, it's a draw.")
    print("Good luck!\n")

def play_game():
    greet_players()
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        # Get player input
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Cell already taken, choose another.")
            except (ValueError, IndexError):
                print("Invalid input, please enter numbers between 0 and 2.")
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns and diagonals for a winner
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    
    return None

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    greet_players()
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        # Get player input
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Cell already taken, choose another.")
            except (ValueError, IndexError):
                print("Invalid input, please enter numbers between 0 and 2.")
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"
if __name__ == "__main__":
    play_game()
# This code implements a simple Tic Tac Toe game for two players.
# Players take turns to place their marks on the board, and the game checks for a winner    or a draw after each turn.
# The game continues until a player wins or the board is full, resulting in a draw.
# The board is printed after each turn to show the current state of the game.
# Players can input their moves by specifying the row and column indices.
# The game handles invalid inputs gracefully, prompting the user to try again.
# The code is structured to be run as a standalone script, allowing players to start a new game easily.
# The game can be extended with features like AI opponents, score tracking, or a graphical interface in the future.
