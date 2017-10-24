import random
import time

marker = {'Παίκτης 1': 'X', 'Computer': 'O', }
triples= ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))

def display_board(board):
    print("+"+41*"="+"+")
    print("|1"+12*" "+"|2"+12*" "+"|3"+12*" "+"|")
    print("|"+6*" "+board[1]+6*" "+"|"+6*" "+board[2]+6*" "+"|"+6*" "+board[3]+6*" "+"|")
    print("|"+13*" "+"|"+13*" "+"|"+13*" "+"|")
    #==============================================
    print("+"+41*"="+"+")
    print("|4"+12*" "+"|5"+12*" "+"|6"+12*" "+"|")
    print("|"+6*" "+board[4]+6*" "+"|"+6*" "+board[5]+6*" "+"|"+6*" "+board[6]+6*" "+"|")
    print("|"+13*" "+"|"+13*" "+"|"+13*" "+"|")
    #==============================================
    print("+"+41*"="+"+")
    print("|7"+12*" "+"|8"+12*" "+"|9"+12*" "+"|")
    print("|"+6*" "+board[7]+6*" "+"|"+6*" "+board[8]+6*" "+"|"+6*" "+board[9]+6*" "+"|")
    print("|"+13*" "+"|"+13*" "+"|"+13*" "+"|")
    print("+"+41*"="+"+")
    
    

def choose_first():
    player=" "
    number=random.randint(1,2)
    if number==1:
        player='Παίκτης 1'
    else:
        player='Computer'
    return player

def display_score(score):
    print("Score is {}".format(score))

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    for triple in triples:
        p1,p2,p3 = triple
        if board[p1]==board[p2]==board[p3]==mark:
            return True
    return False
    
    

def board_check(board):
    check=False
    if board[1]==" " or board[2]==" " or board[3]==" " or board[4]==" " or board[5]==" " or board[6]==" " or board[7]==" " or board[8]==" " or board[9]==" ":
        return False
    else:
        return True
 
def player_choice(board, turn):
    topofesia=" "
    topofesia=input("{} , Choice a box between 1-9:".format(turn))
    while True:
        if topofesia not in "1 2 3 4 5 6 7 8 9":
            topofesia=input("Error, Choice a box between 1-9:")
        else:
            if board[int(topofesia)]!=" ":
                print("The "+topofesia+" is completed, choice another box.")
                topofesia=input("{} , Choice a box between 1-9:".format(turn))
            else:
                return int(topofesia)


def replay():
    ask=input("Do you want to play again? Yes/No\n")
    if ask=="Yes" or ask=="yes":
        return True
    else: return False


def next_player(turn):
    if turn=='Παίκτης 1':
        return 'Computer'
    else:
        return 'Παίκτης 1'

def available(board):
    return [s for s in range(1,10) if board[s] == " "]


def checkPartial(board, player):
    for triple in triples:
        p1,p2,p3 = triple
        if board[p1] == board[p2] == player and board[p3] == " ":
            return p3
        elif board[p2] == board[p3] == player and board[p1] == " ":
            return p1
        elif board[p3] == board[p1] == player and board[p2] == " ":
            return p2
    return None


def randomPosition(board):
    nbMoves = board.count("X")
    if nbMoves >= 2:
        position = checkPartial(board, "X")
        if position is not None:
            return position
    return random.choice(available(board))


def main():
    score = {}
    print('Αρχίζουμε!\nΓίνεται κλήρωση ', end = '')
    for t in range(10):
        print(".", flush='True', end=' ')
        time.sleep(0.2)
    print()
    turn = choose_first() 
    print("\nΟ " + turn + ' παίζει πρώτος.')
    first = turn
    game_round = 1
    while True:
        theBoard = [' '] * 10 
        game_on = True
        while game_on:
            if turn == "Computer":
                print("Computer playing:")
                positions = available(theBoard)
                position = randomPosition(theBoard)
            else:
                display_board(theBoard)
                position = player_choice(theBoard, turn)
            place_marker(theBoard, marker[turn], position) 
            if win_check(theBoard, marker[turn]):
                display_board(theBoard)
                print('Νίκησε ο '+ turn)
                score[turn] = score.get(turn, 0) + 1
                game_on = False
            elif board_check(theBoard): 
                display_board(theBoard)
                print('Ισοπαλία!')
                game_on = False
            else:
                turn = next_player(turn)
        if not replay():
            ending = ''
            if game_round>1 : ending = 'υς'
            print("Μετά {} γύρο{}".format(game_round, ending))
            display_score(score)
            break
        else :
            game_round += 1
            turn = next_player(first) 
            first = turn
main()
