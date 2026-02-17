import random

def create_board():
    return [[' ' for i in range(3)] for j in range(3)]

def draw_bord(bord):
    print()
    for i in range(3):
        print(f'{bord[i][0]} {chr(9553)} {bord[i][1]} {chr(9553)} {bord[i][2]}')
        if i < 2:
            print(chr(9552),chr(9580),chr(9552),chr(9580),chr(9552))
    print()

def coord(cell):
    match cell:
        case 1:
            return(0,0)
        case 2:
            return(0,1)
        case 3:
            return(0,2)
        case 4:
            return(1,0)
        case 5:
            return(1,1)
        case 6:
            return(1,2)
        case 7:
            return(2,0)
        case 8:
            return(2,1)
        case 9:
            return(2,2)

def check(boar, *cells):
    x1,y1 = coord(cells[0])
    x2,y2 = coord(cells[1])
    x3,y3 = coord(cells[2])
    return boar[x1][y1] == boar[x2][y2] == boar[x3][y3] != ' '

def checkwin(board):
    if board[0][0] != ' ':
        if check(board,1,2,3):
            return board[0][0]
        if check(board,1,4,7):
            return board[0][0]
        if check(board,1,5,9):
            return board[0][0]
    if board[0][1] != ' ':
        if check(board,2,5,8):
            return board[0][1]
    if board[0][2] != ' ':
        if check(board,3,6,9):
            return board[0][2]
        if check(board,3,5,7):
            return board[0][2]
    if board[1][0] != ' ':
        if check(board,4,5,6):
            return board[1][0]
    if board[2][0] != ' ':
        if check(board,7,8,9):
            return board[2][0]

def bot_easy(bord):
    while True:
        x,y = coord(random.randint(1,9))
        if bord[x][y] == ' ':
            return x,y

def bot_medium(bord, bot, user):
    for i in range(1,10):
        x,y = coord(i)
        if bord[x][y] == ' ':
            bord[x][y] = bot
            if checkwin(bord) == bot:
                bord[x][y] = ' '
                return x,y
            bord[x][y] = ' '
    for i in range(1,10):
        x,y = coord(i)
        if bord[x][y] == ' ':
            bord[x][y] = user
            if checkwin(bord) == user:
                bord[x][y] = ' '
                return x,y
            bord[x][y] = ' '
    return bot_easy(bord)

def bot_hard(bord, bot, user):
    if bord[1][1] == ' ':
        return 1,1
    for i in [1,3,7,9]:
        x,y = coord(i)
        if bord[x][y] == ' ':
            return x,y
    return bot_medium(bord, bot, user)

def choose_level():
    while True:
        l = input("levels 1-2-3 ")
        if l in ['1','2','3']:
            return int(l)

def choose_mode():
    while True:
        m = input(" 1 - bot, 2 - player ")
        if m in ['1','2']:
            return m

mode = choose_mode()
level = choose_level() if mode == '1' else None

while True:
    bord = create_board()
    draw_bord(bord)
    count = 9
    player = 'X'

    while count > 0:
        if mode == '1' and player == 'O':
            if level == 1:
                x,y = bot_easy(bord)
            elif level == 2:
                x,y = bot_medium(bord,'O','X')
            else:
                x,y = bot_hard(bord,'O','X')
            print(f'Bot {3*x+y+1}')
        else:
            step = input(f'{player} 1-9 ')
            if step not in '123456789':
                continue
            x,y = coord(int(step))
            if bord[x][y] != ' ':
                continue

        bord[x][y] = player
        draw_bord(bord)
        count -= 1

        win = checkwin(bord)
        if win:
            print(f'win {win}')
            break

        player = 'O' if player == 'X' else 'X'

    if not win:
        print('draw')

    if input("y-n ").lower() == 'y':
        mode = choose_mode()
        if mode == '1':
            level = choose_level()

    print("\nnew game\n")




