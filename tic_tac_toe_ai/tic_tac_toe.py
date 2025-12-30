# TIC TAC TOE: HUMAN (X) vs AI (O)
# AI uses Minimax Algorithm (Unbeatable)

# -------------------------------
# Board representation
# -------------------------------
board = [' ' for _ in range(9)]

# -------------------------------
# Print the board
# -------------------------------
def print_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

# -------------------------------
# Check winner
# -------------------------------
def check_winner(player):
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# -------------------------------
# Check draw
# -------------------------------
def is_draw():
    return ' ' not in board

# -------------------------------
# Human move
# -------------------------------
def human_move():
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move < 0 or move > 8:
                print("Please enter a number between 0 and 8.")
            elif board[move] != ' ':
                print("That position is already taken.")
            else:
                board[move] = 'X'
                break
        except ValueError:
            print("Please enter a valid number.")

# -------------------------------
# Minimax algorithm
# -------------------------------
def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = 100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score

# -------------------------------
# AI move
# -------------------------------
def ai_move():
    best_score = -100
    best_move = 0

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = 'O'

# -------------------------------
# Main game loop
# -------------------------------
print("TIC TAC TOE")
print("You are X | AI is O")
print("Positions: 0 to 8")

while True:
    print_board()
    human_move()

    if check_winner('X'):
        print_board()
        print("🎉 You win!")
        break

    if is_draw():
        print_board()
        print("It's a draw!")
        break

    ai_move()

    if check_winner('O'):
        print_board()
        print("🤖 AI wins!")
        break
