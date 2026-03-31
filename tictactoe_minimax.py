import math

def init_board():
    return [' '] * 9

def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print("\n")

def check_winner(board):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    return None

def is_terminal(board):
    return check_winner(board) is not None or ' ' not in board

def utility(board):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    return 0

def get_moves(board):
    return [i for i in range(9) if board[i] == ' ']

def make_move(board, index, player):
    new_board = board[:]
    new_board[index] = player
    return new_board

# Minimax with Alpha-Beta
def minimax(board, depth, is_max, alpha, beta):
    if is_terminal(board):
        score = utility(board)
        print(f"Terminal reached: Utility = {score}")
        return score

    if is_max:
        max_eval = -math.inf
        print(f"\nMAX node at depth {depth} | α={alpha}, β={beta}")
        
        for move in get_moves(board):
            eval = minimax(make_move(board, move, 'X'), depth+1, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)

            print(f"MAX evaluating move {move} → score {eval} | α={alpha}, β={beta}")

            # Alpha-Beta cutoff
            if beta <= alpha:
                print(">>> Alpha-Beta Cutoff at MAX node!")
                break

        return max_eval

    else:
        min_eval = math.inf
        print(f"\nMIN node at depth {depth} | α={alpha}, β={beta}")
        
        for move in get_moves(board):
            eval = minimax(make_move(board, move, 'O'), depth+1, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)

            print(f"MIN evaluating move {move} → score {eval} | α={alpha}, β={beta}")

            # Alpha-Beta cutoff
            if beta <= alpha:
                print(">>> Alpha-Beta Cutoff at MIN node!")
                break

        return min_eval

# Best move for agent
def best_move(board, player):
    best_val = -math.inf if player == 'X' else math.inf
    best_move_index = None

    print(f"\nFinding best move for {player}...")

    for move in get_moves(board):
        new_board = make_move(board, move, player)

        if player == 'X':
            move_val = minimax(new_board, 0, False, -math.inf, math.inf)
            if move_val > best_val:
                best_val = move_val
                best_move_index = move
        else:
            move_val = minimax(new_board, 0, True, -math.inf, math.inf)
            if move_val < best_val:
                best_val = move_val
                best_move_index = move

        print(f"Move {move} → Utility {move_val}")

    print(f"Best Move for {player}: {best_move_index} with score {best_val}")
    return best_move_index

def play_game():
    board = init_board()
    current_player = 'X'

    print("Starting Tic-Tac-Toe (Minimax + Alpha-Beta)\n")

    while not is_terminal(board):
        print_board(board)

        move = best_move(board, current_player)
        board = make_move(board, move, current_player)

        print(f"{current_player} plays at position {move}")

        current_player = 'O' if current_player == 'X' else 'X'

    print_board(board)

    winner = check_winner(board)
    if winner:
        print(f"Winner: {winner}")
    else:
        print("Game Draw!")

play_game()