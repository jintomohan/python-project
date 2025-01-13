def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Check for a win
def check_win(board, player):
    win_conditions = [
        [0, 1, 2],  # Horizontal
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],  # Vertical
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],  # Diagonal
        [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Check for a tie
def check_tie(board):
    return all(spot != " " for spot in board)

# Main game function
def play_game():
    board = [" " for _ in range(9)]  # Empty game board
    current_player = "X"
    game_running = True

    print("Welcome")
    print_board(board)

    while game_running:
        # Player input
        try:

            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = current_player
            else:
                print("This spot is already taken! Try again.")
                continue
        except (IndexError, ValueError):
            print("Invalid move! Please enter a number between 1 and 9.")
            continue

        # Display the board
        print_board(board)

        # Check for a win
        if check_win(board, current_player):
            print(f"Congratulations! Player {current_player} wins!")
            game_running = False
        # Check for a tie
        elif check_tie(board):
            print("It's a tie!")
            game_running = False
        else:
            # Switch player
            current_player = "O" if current_player == "X" else "X"

if name == "main":
   play_game()
