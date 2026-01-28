# task 1

number = int(input('number : '))
for i in range(1, 10):
    multiplication = number * i
    print(number, '*', i, '=', multiplication)


# task 2

# res = input('''
#         [1] - USD --> UAH
#         [2] - UAH --> USD
#         [0] - Bye
# ''')
# if res == '0':
#     print('bye')
# if res == "1":
#     usd = int(input("number --> "))
#     print(usd * 42,'grivni')
# elif res == '2':
#     usd = int(input("number --> "))
#     print(usd / 42,'dollars')


# task 3

# num1 = int(input('початок діапазону : '))
# num2 = int(input('кінець діапазону : '))
# num = int(input('num : '))
# while num < num1 or num > num2:
#     print('введи повторно число')
#     num = int(input('num : '))


# for i in range(num1, num2 +1):
#     if i == num:
#         print(f'!{i}!', end='')
#     else:
#         print(i, end='')

# task 4

# max = 0
# number = int(input('number : '))
# for i in range(1, number+1):
#     num = int(input('numb : '))
#     print(num)

#     if max < num:
#         max = num

# print('max -->', max)


# task 5

from datetime import datetime
import random

randomm = random.randint(1, 500)

start = input('''
#         ----Гра вгадай число (від 1 до 500)----
              [0] --> stop
# ''')

print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)
s = datetime.now()

while True:
    for i in range(1, 501):
       number = int(input('number -->'))
    if number == 0:
        break
    if number < randomm:
     print('число менше')
    elif number > randomm:
     print('число більше')
    elif number == randomm:
       print('ти вгадав число')
       break
       
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)


# task 6

# figure = input('квадрат чи прямокутник -->')
# sumvol = input('sumvol')
# if figure == "квадрат":
#     length = int(input('lenght --> '))

#     for i in range(length):
#         for j in range(length):
#             print(sumvol, end='')            
#         print(sumvol)
# elif figure == "прямокутник":
#     width =  int(input('wigth --> '))
#     height = int(input('height --> '))  

#     for i in range(height):
#         for j in range(width):
#             print(sumvol, end='')
#         print(sumvol)    
# else:
#     print('невірна фігура')