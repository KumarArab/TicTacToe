import random

board = ['-','-','-'
        ,'-','-','-',
         '-','-','-',]

def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])

def check_empty_area(board):
    l = []
    for i in range(len(board)):
        if board[i] == '-':
            l.append(i)
    return l

def user_choice(choice):
    board[choice] = 'X'

def random_choice(board):
    available = check_empty_area(board)
    choice = random.choice(available)
    board[choice] = '0'
    print("Your Turn:")

def row_win():
    b = False
    if board[0] == board[1] == board[2] == '0' or board[3] == board[4] == board[5] == '0' or board[6] == board[7] == board[8] == '0' or board[0] == board[3] == board[6] == '0' or board[1] == board[4] == board[7] == '0' or board[2] == board[5] == board[8] == '0' or board[0] == board[4] == board[8] == '0' or board[2] == board[4] == board[6] == '0' :
        print("Computer Won")
        b = True
    elif board[0] == board[1] == board[2] == 'X' or board[3] == board[4] == board[5] == 'X' or board[6] == board[7] == board[8] == 'X' or board[0] == board[3] == board[6] == 'X' or board[1] == board[4] == board[7] == 'X' or board[2] == board[5] == board[8] == 'X' or board[0] == board[4] == board[8] == 'X' or board[2] == board[4] == board[6] == 'X' :
        print("You Won")
        b = True
    elif board[0] == board[1] == board[2] == board[3] == board[4] == board[5] == board[6] == board[7] == board[8] != '-':
        print("Draw")
        b = True
    return b
    
#main method

win = False
while not win:
    display_board()
    u = int(input("Enter the your position: "))
    user_choice(u-1)
    random_choice(board)
    win = row_win()



