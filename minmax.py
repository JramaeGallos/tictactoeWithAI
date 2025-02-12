# Jramae A. Gallos
# CMSC 170 X4L
# Exercise 10

init_board = {0: '', 1: '', 2: '',
         3: '', 4: '', 5: '',
         6: '', 7: '', 8: ''}

ai= ""
user= ""

# function that checks if the current tile in the board is free
def is_free(brd, pos):
    if brd[pos] == '':
        return True
    else:
        return False

# check which of player has won the game
def which_player_won(brd, player):
    # horizontal
    if brd[0] == brd[1] and brd[0] == brd[2] and brd[0] == player:
        return True
    elif (brd[3] == brd[4] and brd[3] == brd[5] and brd[3] == player):
        return True
    elif (brd[6] == brd[7] and brd[6] == brd[8] and brd[6] == player):
        return True

    # vertical
    elif (brd[0] == brd[3] and brd[0] == brd[6] and brd[0] == player):
        return True
    elif (brd[1] == brd[4] and brd[1] == brd[7] and brd[1] == player):
        return True
    elif (brd[2] == brd[5] and brd[2] == brd[8] and brd[2] == player):
        return True
    
    # diagonal
    elif (brd[0] == brd[4] and brd[0] == brd[8] and brd[0] == player):
        return True
    elif (brd[2] == brd[4] and brd[2] == brd[6] and brd[2] == player):
        return True
    else:
        return False

# function that checks if the current state of the game is draw
# if there are no available spaces in the board; then draw
def if_draw(brd):
    for key in brd.keys():
        if (brd[key] == ''):
            return False
    return True

def check_win(brd):
    # horizontal
    if (brd[0] == brd[1] and brd[0] == brd[2] and brd[0] != ''):
        return (True, brd[0])
    elif (brd[3] == brd[4] and brd[3] == brd[5] and brd[3] != ''):
        return (True, brd[3])
    elif (brd[6] == brd[7] and brd[6] == brd[8] and brd[6] != ''):
        return (True, brd[6])

    # vertical
    elif (brd[0] == brd[3] and brd[0] == brd[6] and brd[0] != ''):
        return (True, brd[0])
    elif (brd[1] == brd[4] and brd[1] == brd[7] and brd[1] != ''):
        return (True, brd[1])
    elif (brd[2] == brd[5] and brd[2] == brd[8] and brd[2] != ''):
        return (True, brd[2])
    
    # diagonal
    elif (brd[0] == brd[4] and brd[0] == brd[8] and brd[0] != ''):
        return (True, brd[0])
    elif (brd[2] == brd[4] and brd[2] == brd[6] and brd[2] != ''):
        return (True, brd[2])
    else:
        return (False, None)

# function that updates the board when changes are made by the ai
def update_game_state(brd, pos, player):
    if is_free(brd, pos):
        brd[pos] = player
    return brd


# function that sets player variables
def set_player(ai_player):
    global ai
    global user
    ai = ai_player
    if ai == "X": user= "O"
    else: user= "X"

# function that simulate the ai turn to move
# ai move is maximized
def ai_move(brd, ai_player):
    set_player(ai_player)
    m = -1000
    best_move= 0

    for key in brd.keys():
        if brd[key] == '':
            brd[key] = ai
            v = minmax(brd, False)
            brd[key] =''

            # check max
            if v > m:
                m = v
                best_move = key
    
    return update_game_state(brd, best_move, ai)


def minmax(brd, isMaximizing):
    # terminal state
    if which_player_won(brd, ai):
        return 1
    elif which_player_won(brd, user):
        return -1
    elif if_draw(brd):
        return 0

    # Maximize state
    if isMaximizing:
        m= -1000
        
        for key in brd.keys():
            if brd[key] == '':
                brd[key]= ai
                v= minmax(brd, False)
                brd[key]= ''

                if (v > m):
                    m = v
        return m

    # Minimize state
    else:
        m= 1000

        for key in brd.keys():
            if brd[key] == '':
                brd[key] = user
                v= minmax(brd, True)
                brd[key] = ''

                if v < m:
                    m = v
        return m    

# function that checks the winner of the game
def get_winner(brd):
    result= check_win(brd)
    winner = None
    if result[0] == True:
        winner = (True, result[1])
    elif if_draw(brd):
        winner = (True, None)
    elif result[0] == False:
        winner = (False, None)

    return winner




