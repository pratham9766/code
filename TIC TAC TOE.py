def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")




def check_winner(board, player):   # this Check rows
    
    for row in board:
        if all([cell == player for cell in row]):
            return True

    
    for col in range(3):        # Check columns
        if all([board[row][col] == player for row in range(3)]):
            return True

            # Check diago
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True

    return False


# -----------------------------------------------------------------------


def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

# -----------------------------------------------------------------------



def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
        col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1
 

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("That place is already occupied. Try again.")
            continue

        print_board(board)

        if check_winner(board, current_player):
            print(f"Congratulations! Player {current_player} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break
# ====================================================================================


            # Switchingg turns
        if current_player == "X":
            current_player = "O"
        
        else:
            current_player = "X"




    play_again = input("Wanna play again? (yes/no): ").lower()
    if play_again == "yes":
        play_tic_tac_toe()
    else:
        print("Thank you for playing Tic-Tac-Toe!")

# Start the game
play_tic_tac_toe()
