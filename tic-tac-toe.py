# import random
# bord = [[' ' for i in range(3)]for j in range(3)]
# # print(bord)

# def draw_bord(bord):
#     print()
#     for i in range(3):
#         print(f'{bord[i][0]} {chr(9553)} {bord[i][1]} {chr(9553)} {bord[i][2]}')
#         if i < 2:
#             # print(chr(9580))
#             print(chr(9552),chr(9580),chr(9552),chr(9580),chr(9552))
#     print()
# draw_bord(bord)


# import random
# bord = [[' ' for i in range(3)]for j in range(3)]

# def row(row, symbol,str = None):
#     for j in range(len(row)):
#         if str == None:
#             print(f'{row[j]}', end='')
#         else:
#             print(f'{str}', end='')
#         if j == len(row) - 1:
#             continue
#         print(symbol,end='')

# def draw_bord(bord):
#     print()
#     for i in range(3):
#         print(f'{bord[i][0]} {chr(9553)} {bord[i][1]} {chr(9553)} {bord[i][2]}')
#         if i < 2:
#             print(chr(9552),chr(9580),chr(9552),chr(9580),chr(9552))

# def coord(cell):
#     match cell:
#         case 1:
#             return(0,0)
#         case 2:
#             return(0,1)
#         case 3:
#             return(0,2)
#         case 4:
#             return(1,0)
#         case 5:
#             return(1,1)
#         case 6:
#             return(1,2)
#         case 7:
#             return(2,0)
#         case 8:
#             return(2,1)
#         case 9:
#             return(2,2)

# def check(boar, *cells):
#     x_1, y_1 = coord(cells[0])
#     x_2, y_2 = coord(cells[1])
#     x_3, y_3 = coord(cells[2])
#     if boar[x_1][y_1] == boar[x_2][y_2] and boar[x_1][y_1] == boar[x_3][y_3]:
#         return True
#     else:
#         return False
    
# def checkwin(board):
#     if board[0][0] != ' ':
#         if check(board,1,2,3):
#             return board[0][0]
#         if check(board,1,4,7):
#             return board[0][0]
#         if check(board,1,5,9):
#             return board[0][0]
#     if board[0][1] != ' ':
#         if check(board,2,5,8):
#             return board[0][1]
#     if board[0][2] != ' ':
#         if check(board,3,6,9):
#             return board[0][2]
#         if check(board,3,5,7):
#             return board[0][2]
#     if board[1][0] != ' ':
#         if check(board,4,5,6):
#             return board[1][0]
#     if board[2][0] != ' ':
#         if check(board,7,8,9):
#             return board[2][0]

# draw_bord(bord)
# count = 9

# user = 'X'
# bot = 'O'
# flag = True

# while count > 0:
#     if flag:
#         step = int(input('enter number cell --> '))
#         x,y = coord(step)
#         if bord[x][y] != ' ':
#             continue
#         bord[x][y] = user
#         flag = False
#         count-=1
#     else:
#         x,y = coord(random.randint(1,9))
#         if bord[x][y] != ' ':
#             continue
#         bord[x][y] = bot
#         flag = True
#         count-=1
#     print()
#     draw_bord(bord)
#     win = checkwin(bord)
#     if win != None:
#         break
# if win == user:
#     print(f'Win user {user}')
# elif win == bot:
#     print(f'Win bot {bot}')
# else:
#     print('draw')




