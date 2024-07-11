import time
import random
import numpy as np
import smart as st

def show_board(board= '123456789'):
    #print(f"\n {board[0]} | {board[1]} | {board[2]} \n-----------\n {board[3]} | {board[4]} | {board[5]} \n-----------\n {board[6]} | {board[7]} | {board[8]} \n")
    print(f"\n {board[6]} | {board[7]} | {board[8]} \n-----------\n {board[3]} | {board[4]} | {board[5]} \n-----------\n {board[0]} | {board[1]} | {board[2]} \n")
def choose_marker():
    player = input('Choose which marker do you want? \n1.X \n2.O\n')
    player = player.upper().strip()
    if player == "1" or player == "X":
        player = "X"
    elif player == "2" or player == "O":
        player = "O"
    else:
        print('Hmmm! something went wrong! Just enter the number or the marker.')
        return choose_marker()
    time.sleep(1)
    print("Who should start the game?")
    time.sleep(1)
    print("You? Hah! OK!")
    time.sleep(1)
    show_board()
    return player



def move(player, board, turn):
    if turn == 'P':
        try:
            cell = int(input('Choose cell: 1-9\n'))
            if board[cell-1] == '-':
                board = board[:cell-1] + player + board[cell:]
            else:
                print('That cell is Full! choose another!')
                return move(player, board, turn)
        except (ValueError, IndexError):
            print('Invalid input! Please choose a valid cell between 1-9.')
            return move(player, board, turn)
    elif turn == 'C':
        next_move = st.find_next_move(board, player)
        if next_move:  
            board = board[:next_move] + player + board[next_move+1:]
        else:
            cells = [i for i in range(9) if board[i] == '-']
            cell = random.choice(cells)
            board = board[:cell] + player + board[cell+1:]
    return board

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


def play_game(player, computer, scores):
    board = '---------'
    turn = 'P'
    show_board(board)
    while not check_status(board):
        if turn == 'P':
            board = move(player, board, turn)
            turn = 'C'
        else:
            board = move(computer, board, turn)
            turn = 'P'
        show_board(board)
        status = check_status(board)
        if status in ['X', 'O']:
            print(f'Player {status} WON!')
            if status == player:
                scores['player'] += 1
            else:
                scores['computer'] += 1
            return
        elif status == 0:
            print("It's a draw!")
            return

def game():
    print("Welcome to TicTacToe for pros!")

    player = choose_marker()
    computer = 'O' if player == 'X' else 'X'
    scores = {'player': 0, 'computer': 0}

    while True:
        play_game(player, computer, scores)
        print(f'SCORES:\nYou: {scores["player"]}\nComputer: {scores["computer"]}\n')
        
        play_again = input("Do you want to play another game? (yes/no): ").strip().lower()
        if play_again not in ('yes', 'y'):
            break

    print("Thanks for playing! Final Scores:")
    print(f'You: {scores["player"]}\nComputer: {scores["computer"]}\n')

game()

