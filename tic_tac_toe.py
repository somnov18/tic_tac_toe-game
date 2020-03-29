import random
print('Welcome to Tic Tac Toe!')

def Display_board(board):


    print('\n'*100)
    print('Positions:')
    print('7'+'|'+'8'+'|'+'9')
    print('-|-|-')
    print('4'+'|'+'5'+'|'+'6')
    print('-|-|-')
    print('1'+'|'+'2'+'|'+'3')
    print('\n'*2)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])

def choose_marker():
    marker=" "
    while not ( marker =='X' or marker =='O'):
        marker=input('player1 choose X or O')
        player1= marker
        if player1 == 'X':
            player2 = 'O'
        else :
            player2 = 'X'
    return (player1,player2)

def chance():

    flip=random.randint(0,1)
    if flip == 0:
        return 'player1'
    else:
        return 'player2'

def space(board,position):
    return board[position]== ' '

def is_available(board):
    position=0
    while not (position in range(1,10) and space(board,position)):
        position=int(input('Enter next position within (1-9):'))
    return position

def win_check(board, mark):

    return ((board[1]==board[2]==board[3]==mark)or
            (board[4]==board[5]==board[6]==mark)or
            (board[7]==board[8]==board[9]==mark)or
            (board[3]==board[6]==board[9]==mark)or
            (board[2]==board[5]==board[8]==mark)or
            (board[1]==board[4]==board[7]==mark)or
            (board[1]==board[5]==board[9]==mark)or
            (board[3]==board[5]==board[7]==mark))


def place(position,marker,board):
    board[position]=marker

def  is_full(board):
    for i in range(1,10):
        if space(board,i):
            return False
    return True

def replay():

    choice= input('want to play again? enter yes or no.').upper()
    return choice == 'YES'
while True:

    board=[' ']*10
    player1_marker,player2_marker = choose_marker()
    turn = chance()
    print(turn+ ' will go first')

    play_game=input('Want to play? y or n?').lower()
    if play_game == 'y':
        game_on = True
    else:
        game_on = False


    while game_on:
        if turn == 'player1':

            #Player 1 Turn
            Display_board(board)
            position = is_available(board)
            place(position,player1_marker,board)

            if win_check(board,player1_marker):
                Display_board(board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if is_full(board):
                    Display_board(board)
                    print('TIE GAME!')
                    break
                else:
                    turn = 'player2'

        else:

            # Player2's turn.
            Display_board(board)
            position = is_available(board)
            place(position,player2_marker,board)

            if win_check(board,player2_marker):
                Display_board(board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                if is_full(board):
                    Display_board(board)
                    print('TIE GAME!')
                    break
                else:
                    turn = 'player1'

    if not replay():
        break
