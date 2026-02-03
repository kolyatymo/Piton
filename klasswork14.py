# функції

# def showMessage(age, id = 0, phone = 'Nonphone', name = 'none'):
#     print(f'Hello {name} \t age --> {age} \t id - {id} \t phone - {phone}')

# showMessage(16)
# showMessage('kolya')
# showMessage(16, 111, '0975214', 'Pavllo')
# showMessage(16, name='pavlo')


# def sum(a,b):
#     return a + b

# res = sum(5,7) / 2
# print(res)

# def sume(a,b):
#     return a + b

# def sube(a,b):
#     return a - b

# def multe(a,b):
#     return a * b

# def dive(a,b):
#     if b != 0:
#         return a / b

# def calculate(a,b,op):
#     match op:
#         case '+':
#             return sume(a,b)
#         case '-':
#             return sube(a,b)
#         case '*':
#             return multe(a,b)
#         case '/':
#             return dive(a,b)
#     print('Error! Not found operation!!')
    

# print(f' 2 + 5 = {calculate(2,5,'+')}')
# print(f' 2 - 5 = {calculate(2,5,'-')}')
# print(f' 2 * 5 = {calculate(2,5,'*')}')
# print(f' 2 / 5 = {calculate(2,5,'/')}')
# print(f' 2 ! 5 = {calculate(2,5,'!')}')

# task 1

# def min_(a,b,c):
#     return min(a,b,c)

# print(f'min = {min_(5,3,7)}')

# task 2

# task 3

# def sume(a,b):
#     return a + b

# def sube(a,b):
#     return a - b

# def multe(a,b):
#     return a * b

# def dive(a,b):
#     if b != 0:
#         return a / b

# def calculate(a,b,op):
#     if op == '+':
#         return sume(a,b)
#     elif op == '-':
#         return sube(a,b)
#     elif op == '*':
#         return multe(a,b)
#     elif op == '/':
#         return dive(a,b)
#     else:
#         return
    
# print(f' 2 + 5 = {calculate(2,5,'+')}')
# print(f' 2 - 5 = {calculate(2,5,'-')}')
# print(f' 2 * 5 = {calculate(2,5,'*')}')
# print(f' 2 / 5 = {calculate(2,5,'/')}')

# task 4

# def simple(a):
#     if a < 2:
#         return False
#     for i in range(2,a):
#         if a % i == 0:
#             return a
# print(simple(12))

# task 5

# def table(a):
#     for i in range(1,10):
#         print(a, '*' ,i, '=', a * i)
#     print()
# for number in range(2,10):
#     table(number)

# task 6

# def div_rem(a,b):
#     resul = a // b
#     return a - resul * b


# task 7

# def sume_(a, b=0,c=0,d=0,i=0):
#     return a + b + c + d + i
# print(sume_(5))
# print(sume_(5,2))
# print(sume_(5,2,4))
# print(sume_(5,4,5,6))
# print(sume_(5,3,4,5,6))


# task 10

# def yers_(year):
#     return year % 4 ==0 and year % 100 != 0 or year % 400 ==0

# def month_(month, year):
#     match month:
#         case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#             return 31
#         case 4 | 6 | 9 | 11:
#             return 30
#         case 2:
#             return 29 if yers_(year) else 28
# def day(day,month,year):
#     day += 1
#     if day > month_(month,year):
#         day = 1
#         month += 1
#     if month > 12:
#         month = 1
#         year += 1
#     return f'{'0' if day < 10 else ''}{day}.{'0' if month < 10 else ''}{month}.{year}'

# def parni_(a,b): # 2-10
#     for i in range(a,b+1,2):
#         if i % 2 == 0:
#             print(i)
# print(parni_(2,10))

# def parni_(a,b): # 2-10
#     for i in range(a,b+1):
#         if i % 2 == 0:
#             print(f'{a} {i} {b}')
# print(parni_(2,10))

# def text_(a,text = ''):
#     print('\t',text)
# print('\t hello 52 dbac h c wh cahc ahs csvd vyvdu vs husv ')
# print('\t \t hello 52 dbac dsi uisu bsiub ')
# print('\t \t \t hello 52 dba')

# def text_(text = ''):
#     print( '\t',text)
# print('hello 52 dbac h c wh cahc ahs csvd vyvdu vs husv ')
# print(' \t hello 52 dbac dsi uisu bsiub ')
# print(' \t \t  hello 52 dba')
