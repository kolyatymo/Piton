# number1 = int(input('numbers -->'))
# number2 = int(input('numbers -->'))
# i = number1
# while i <= number2:
#     if i % 7 == 0:
#      print(i)
#     i+=1


# number1 = int(input('numbers -->'))
# number2 = int(input('numbers -->'))
# i = number1
# while i <= number2:
#     print(i)
#     i += 1
# print()

# i = number2
# while i >= number1:
#     print(i)
#     i -=1
# print()

# i = number1
# while i <= number2:
#     if i % 7 ==0:
#         print(i)
#     i += 1

# count = 0
# i = number1
# while i <= number2:
#     if i % 5 ==0:
#         count +=1
#     i +=1
# print(count)

# number1 = int(input('numbers -->'))
# number2 = int(input('numbers -->'))
# i = number1
# while i <= number2:
#     if i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     if i % 3 ==0 and i % 5 ==0:
#         print('Fizz Buzz')
#     else:
#         print(i)
#     i +=1

# number1 = int(input('numbers -->'))
# number2 = int(input('numbers -->'))
# krok = int(input('krok -->'))
# a = input('blablabla --')
# i = number1
# if a == 'pered':
#     while i <= number2:
#         print(i,end='')
#         i += krok
# elif a == 'nazad':
#     i = number2
#     while i >= number1:
#         print(i)
#         i -= krok


# number1 = int(input('numbers -->'))
# number2 = int(input('numbers -->'))
# if number1 > number2:
#     number1, number2 = number2,number1
# dobytok = 1
# i = number1
# while i <= number2:
#     if i % 4 ==0 and i % 6 != 0:
#         dobytok *= i
#     i +=1
# print(dobytok)


# import re

# str_1 = '123'
# str_2 = '623'
# str_3 = 'Lorem** 123'

# print(re.search('[0-9]',str_1))
# print(re.search('[0-9]',str_2))
# print(re.search('[0-9]',str_3))
# print()

# print(re.search('[\w]',str_1))
# print(re.search('[\w]',str_2))
# print(re.search('[\w]',str_3))
# print()

# match = re.search('[a-zA-Z]{3,10}\** \w+',str_3)

# if match:
#     print('find')
#     print(match.start(), match.end(), match.group(0))
# else:
#     print('not')
# print()

# print(re.search('\w$',str_1))
# print(re.search('\w$',str_2))
# print(re.search('\w{3}$',str_3))
# print()

# print(re.search('^\w',str_1))
# print(re.search('^\w',str_2))
# print(re.search('^\w{3}',str_3))

# text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'

# line = re.findall(r'[ .,]\w{4}[ .,]',text)

# for i in line:
#     print(i)

# import string
# import random

# print('-'.join(random.sample(string.ascii_uppercase,10)))

# user = input('enter -->')
# print(len(user))


# user = input('enter -->')
# user1 = input('enter1 -->')
# count = 0
# i = 0
# for i in user:
#     if user1 == i:
#         count +=1
# print(count)

# user = input('enter -->')
# revers = ''
# for i in user:
#     revers = i + revers
# print(revers)

# import re

# user = input('enter -->')
# user1 = input('enter1 -->') 

# line = re.findall(user1,user)
# print(len(line))

# Створення порожнього поля
# bord = [[' ' for i in range(3)] for j in range(3)]

# # Функція для відображення рядка (необов'язково, можна залишити для майбутнього)
# def row(row, symbol, str=None):
#     for j in range(len(row)):
#         if str is None:
#             print(f'{row[j]}', end='')
#         else:
#             print(f'{str}', end='')
#         if j != len(row) - 1:
#             print(symbol, end='')

# # Функція для відображення поля
# def draw_bord(bord):
#     print()
#     for i in range(3):
#         print(f' {bord[i][0]} ║ {bord[i][1]} ║ {bord[i][2]} ')
#         if i < 2:
#             print('───╫───╫───')
#     print()

# # Функція для перетворення номера клітинки на координати
# def coord(cell):
#     match cell:
#         case 1: return (0,0)
#         case 2: return (0,1)
#         case 3: return (0,2)
#         case 4: return (1,0)
#         case 5: return (1,1)
#         case 6: return (1,2)
#         case 7: return (2,0)
#         case 8: return (2,1)
#         case 9: return (2,2)
#         case _: return (-1,-1)

# # Перевірка трьох клітинок на однаковий символ
# def check(boar, *cells):
#     x1, y1 = coord(cells[0])
#     x2, y2 = coord(cells[1])
#     x3, y3 = coord(cells[2])
#     if boar[x1][y1] == boar[x2][y2] == boar[x3][y3] != ' ':
#         return True
#     return False

# # Перевірка перемоги
# def checkwin(board):
#     wins = [
#         (1,2,3), (4,5,6), (7,8,9),
#         (1,4,7), (2,5,8), (3,6,9),
#         (1,5,9), (3,5,7)
#     ]
#     for a, b, c in wins:
#         if check(board, a, b, c):
#             x, y = coord(a)
#             return board[x][y]
#     return None

# # Відображаємо порожнє поле
# draw_bord(bord)

# count = 9
# players = ['X', 'O']
# turn = 0  # чергує гравців

# while count > 0:
#     player = players[turn % 2]
#     try:
#         step = int(input(f'Гравець {player}, введіть номер клітинки (1-9): '))
#     except ValueError:
#         print("Введіть число від 1 до 9!")
#         continue

#     x, y = coord(step)
#     if (x, y) == (-1,-1):
#         print("Некоректна клітинка! Введіть від 1 до 9.")
#         continue
#     if bord[x][y] != ' ':
#         print("Ця клітинка зайнята! Оберіть іншу.")
#         continue

#     bord[x][y] = player
#     draw_bord(bord)
#     count -= 1

#     win = checkwin(bord)
#     if win:
#         print(f'Вітаємо! Гравець {win} переміг!')
#         break

#     turn += 1

# if not win:
#     print('Нічия!')



import random

# Функція для створення порожнього поля
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
    x1, y1 = coord(cells[0])
    x2, y2 = coord(cells[1])
    x3, y3 = coord(cells[2])
    if boar[x1][y1] == boar[x2][y2] == boar[x3][y3] != ' ':
        return True
    return False

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

# --- Боти ---
def bot_easy(bord, bot_symbol):
    while True:
        x,y = coord(random.randint(1,9))
        if bord[x][y] == ' ':
            return x,y

def bot_medium(bord, bot_symbol, user_symbol):
    # спробувати виграти
    for a in range(1,10):
        x,y = coord(a)
        if bord[x][y] == ' ':
            bord[x][y] = bot_symbol
            if checkwin(bord) == bot_symbol:
                bord[x][y] = ' '
                return x,y
            bord[x][y] = ' '
    # спробувати заблокувати користувача
    for a in range(1,10):
        x,y = coord(a)
        if bord[x][y] == ' ':
            bord[x][y] = user_symbol
            if checkwin(bord) == user_symbol:
                bord[x][y] = ' '
                return x,y
            bord[x][y] = ' '
    return bot_easy(bord, bot_symbol)

def bot_hard(bord, bot_symbol, user_symbol):
    # виграти
    for a in range(1,10):
        x,y = coord(a)
        if bord[x][y] == ' ':
            bord[x][y] = bot_symbol
            if checkwin(bord) == bot_symbol:
                bord[x][y] = ' '
                return x,y
            bord[x][y] = ' '
    # заблокувати користувача
    for a in range(1,10):
        x,y = coord(a)
        if bord[x][y] == ' ':
            bord[x][y] = user_symbol
            if checkwin(bord) == user_symbol:
                bord[x][y] = ' '
                return x,y
            bord[x][y] = ' '
    # центр
    if bord[1][1] == ' ':
        return 1,1
    # кути
    for a in [1,3,7,9]:
        x,y = coord(a)
        if bord[x][y] == ' ':
            return x,y
    # інші клітинки
    for a in range(1,10):
        x,y = coord(a)
        if bord[x][y] == ' ':
            return x,y

# --- Вибір рівня гри ---
def choose_level():
    while True:
        level = input("Оберіть рівень бота (1-Легкий, 2-Середній, 3-Складний): ")
        if level in ['1','2','3']:
            return int(level)
        print("Введіть 1, 2 або 3!")

level = choose_level()


while True:
    bord = create_board()
    draw_bord(bord)
    count = 9
    user = 'O'
    bot = 'X'
    flag = True 

    while count > 0:
        if flag:
            try:
                step = int(input('Ваш хід (1-9): '))
            except ValueError:
                print("Введіть число від 1 до 9!")
                continue
            x,y = coord(step)
            if (x,y) == (-1,-1):
                print("Некоректна клітинка!")
                continue
            if bord[x][y] != ' ':
                print("Клітинка зайнята!")
                continue
            bord[x][y] = user
            flag = False
        else:
            if level == 1:
                x,y = bot_easy(bord, bot)
            elif level == 2:
                x,y = bot_medium(bord, bot, user)
            else:
                x,y = bot_hard(bord, bot, user)
            bord[x][y] = bot
            print(f'Бот ({bot}) ходить на клітинку {3*x + y + 1}')
            flag = True

        draw_bord(bord)
        count -= 1
        win = checkwin(bord)
        if win != None:
            break

    if win == user:
        print(f'Ви виграли! ({user})')
    elif win == bot:
        print(f'Бот виграв! ({bot})')
    else:
        print('Нічия!')

    change = input("Хочете поміняти рівень бота? (y/n): ").lower()
    if change == 'y':
        level = choose_level()
    print("\n--- Нова гра починається ---\n")




