import math

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("-" * 9)

def is_winner(board, player):
    for i in range(3):
        if board[i] == [player] * 3:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, 'X'):
        return 1
    if is_winner(board, 'O'):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score

    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def best_move():
    best_score = -math.inf
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def main():
    
    while True:
        print_board(board)

        try:
            row, col = map(int, input("Enter your move (row and column 0-2): ").split())
        except ValueError:
            print("Invalid input! Enter two numbers (0-2) separated by space.")
            continue

        if row not in range(3) or col not in range(3) or board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue

        board[row][col] = 'O'

        if is_winner(board, 'O'):
            print_board(board)
            print("You win! ")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw! ")
            break

        ai_move = best_move()
        if ai_move:
            board[ai_move[0]][ai_move[1]] = 'X'
            print("AI has made its move. ")

        if is_winner(board, 'X'):
            print_board(board)
            print("AI wins! ")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

main()
