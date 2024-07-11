import numpy as np

def check_status(board):
    board_array = np.array(list(board)).reshape(3, 3)
    rows = [board_array[i, :] for i in range(3)]
    cols = [board_array[:, i] for i in range(3)]
    diagonals = [board_array.diagonal(), np.fliplr(board_array).diagonal()]
    
    for player in ['X', 'O']:
        for line in rows + cols + diagonals:
            if np.all(line == player):
                return player # X or O wins
    
    if '-' not in board:
        return 0 #Draw
    
    return None #game is still on 

def find_empty_cells(board):
        return [i for i in range(9) if board[i] == '-']

def switch_player(current_player):
        return 'X' if current_player == 'O' else 'O'

#Generate all possible states
def get_states(board, current_player,):
    def generate_states(board, player, steps, moves, collected_states):
        empty_cells = find_empty_cells(board)
        winner = check_status(board)
        
        if winner:
            result = 'win' if winner == current_player else 'lose'
            if winner == 0:
                result = 'draw'
            collected_states[board] = (steps, result, moves)
            return
        
        if not empty_cells:
            collected_states[board] = (steps, 'draw', moves)
            return
        
        for cell in empty_cells:
            new_board = board[:cell] + player + board[cell+1:]
            new_moves = moves + [(player, cell)]
            generate_states(new_board, switch_player(player), steps + 1, new_moves, collected_states)

    all_states = {}
    generate_states(board, current_player, 0, [], all_states)
    return all_states

#Get all winning states from the dictionary of states
def get_winning_states(states_dict):
    winning_states = {}
    for board, (steps, result, moves) in states_dict.items():
        if result == 'win':
            winning_states[board] = (steps, result, moves)
    # Sort the winning states by the number of steps in increasing order
    sorted_winning_states = dict(sorted(winning_states.items(), key=lambda item: item[1][0]))
    return sorted_winning_states

# Check if a given state matches the current board
def matcher(board, state):
    for i in range(9):
        if board[i] != '-' and board[i] != state[i]:
            return False
    return True

def find_next_move(board, player,):
    all_states = get_states(board, player)
    sorted_winning_states = get_winning_states(all_states)
    
    for state, (steps, result, moves) in sorted_winning_states.items():
        if matcher(board, state):
            for move in moves:
                if move[0] == player and board[move[1]] == '-':
                    return move[1]
    return None

