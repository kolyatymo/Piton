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


