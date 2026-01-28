# task 1

# user = input('numbers --> ').split()
# even = 0
# odd = 0
# for i in user:
#     if int(i) % 2 == 0:
#         even +=1
#     if int(i) % 2:
#         odd +=1
# print('парні числа', even)
# print('непарні числа', odd)

# task 2

# user = [int(i) for i in input('numbers --> ').split()]
# print('Max --> ',max(user))
# print('Min --> ',min(user))

# task 3

# import random
# a = []
# negative = 0
# positive = 0
# zero = 0
# for i in range(10):
#     a.append(random.randint(-10,10))
# print(a)

# min_ = min(a)
# max_ = max(a) 
# print('Min --> ',min_)
# print('Max --> ',max_)
# for j in a:
#     if j < 0:
#         negative +=1
#     elif j > 0:
#         positive +=1
#     elif j == 0:
#         zero +=1
# print('кількість відємних числ --> ',negative)
# print('кількість додатніх числ --> ',positive)
# print('числа = 0 --> ',zero)

# task 4

# user = [int(i) for i in input('numbers --> ').split()]
# num = int(input('number --> '))
# for i in user:
#     if i >= num:
#         print(i)

# task 5

# while True:
#     user = input(' --> ',)
#     if user == 'stop':
#         break
#     q = ['+','-','/','*']
#     for i in q:
#         if i in user:

#             a ,b = user.split(i)
#             a = float(a)
#             b = float(b)
        
#             if i == '+':
#                 print(a+b)
#             elif i == '-':
#                 print(a-b)
#             elif i == '*':
#                 print(a*b)
#             elif i == '/':
#                 print(a/b)
        

# task 6

# import random

# numbers = [random.randint(-10,10) for i in range(10)]

# resul = []

# print('before --> ',numbers)
# print()
# for j in numbers:
#     if j < 0:
#         resul.append(j)
# for q in numbers:
#     if q >= 0:
#         resul.append(q)
# print('result --> ',resul)


        
# task 1

# number = [int(i) for i in input('numbers -->').split()]
# print('sume =', sum(number))
# print('average =', sum(number) / len(number))

# task 2

# text = input('text -->').split()
# num = int(input('num -->'))
# count = 0
# for i in text:
#     if int(i) == num:
#         count +=1
# print(count)

# task 3

# number = input('number -->').split()
# count = 0
# for i in number:
#     if int(i) > 0:
#         count += int(i)
# print(count)

# task 4

# number = input('number -->').split()
# count = 0
# for i in number:
#     if int(i) % 2 == 0:
#         count += len(i)
# print(count)

# task 5

# text = 'Yesterday! 2 evening. I walked through. a quiet street 2 and 2 thought 1 about, 5 simple! things.'
# num = '1234567890'
# num1 = ',.'
# num2 = '!'
# count = 0
# count1 = 0
# count2 = 0
# for i in text:
#     if i in num:
#         count += 1
#     elif i in num1:
#         count1 +=1
#     elif i in num2:
#         count2 +=1
# print('в тексті',count,'цифр')
# print('в тексті',count1,'розділових знаків')
# print('в тексті',count2,'знаків оклику')
# print()
# print(text.title())

# tasl 6

# number = input('number -->').split()
# print(set(number))