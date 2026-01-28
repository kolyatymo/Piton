
# color = ['red', 'yellow', 'blue', 'orange']
# print(type(color), id(color), color, sep='\n')

# print(color[1])
# color[1] = 'black'
# print(color)

# for item in color:
#     print(item)
#     item = 'test'

# print(color)

# # for i in range(len(color)):
# #     color[i] = 'test'

# # print(color)

# print(color[::2])

# print('\n\n====================================\n\n')

# # + новий елемент в кінець
# print(f'\t before :: {color}')
# color.append('purple')
# print(f'\t after :: {color}')

# print('\n\n====================================\n\n')

# # + новий елемент в вибране місце
# print(f'\t before :: {color}')
# color.insert(2,'purple')
# print(f'\t after :: {color}')

# print('\n\n====================================\n\n')

# # додає списки в один в кінець
# print(f'\t before :: {color}')
# color.extend(['gold', 'lime', 'green'])
# print(f'\t after :: {color}')

# print('\n\n====================================\n\n')

# # видаляє елемент в списку
# print(f'\t before :: {color}')
# color.pop(4)
# print(f'\t after :: {color}')

# print('\n\n====================================\n\n')

# # видалення за значенням
# print(f'\t before :: {color}')
# color.remove('blue')
# print(f'\t after :: {color}')

# print('\n\n====================================\n\n')


# print(f'\t before :: {color}')
# if 'blue' in color:
#     color.remove('blue')
# print(f'\t after :: {color}')

# print('\n\n====================================\n\n')


# # print(f'\t before :: {color}')
# # color.clear()
# # print(f'\t after :: {color}')

# print('\n\n====================================\n\n')

# # пошук індекса по значенню
# print('index --> ',color.index('lime'))

# for i in range(3):
#     color.append('red')

# print(f'\t after :: {color}')
# print('\t Number of the word', color.count('red'))
# print('\n\n====================================\n\n')

# color.reverse()
# print(color)

# print('\n\n====================================\n\n')

# # сортування рядків по коду
# color.sort()
# print(color)

# print('\n\n====================================\n\n')

# # сортування в порядку спадання
# color.sort(reverse=True)
# print(color)

# print('\n\n====================================\n\n')

# # copy = color
# # print(f'original :: {color}')
# # print(f'clone :: {copy}')

# # print('\n\n====================================\n\n')

# copy = color.copy()
# print(f'original :: {color}')
# print(f'clone :: {copy}')

# print('\n\n====================================\n\n')

# copy[2] = 'violet'
# print(f'original :: {color}')
# print(f'clone :: {copy}')

# print('\n\n====================================\n\n')

# import random

# # number = []

# # for i in range(10):
# #     number.append(random.randint(1,10))
# # print(number)

# number = [random.randint(1,10) for i in range(10)]

# print(number)


# for i in range(1,4):
#     for j in range(1,4):
#         number.append(i*j)
# print(number)

# number = [i * 100 + j * 10 + q for i in range(1,4) for j in range(1,4) for q in range(4)]



# num = [str(i) + str(j) + str(q) if i != j != q != i else None for i in range(10) for j in range(10) for q in range(10)]


# # set - видаляє повтор

# print(len(num))
# num = set(num)
# print(num)
# num.remove(None)
# print(len(num))

# marks = input('enter marks --> ').split()
# sum = 0 
# for i in marks:
#     sum += int(i)
# print(sum)

# marks =[int(i)for i in input('enter marks --> ').split()]
# print(sum(marks))
# print(min(marks))
# print(max(marks))
# print(sum(marks) / len(marks))
# print(sorted(marks))
# print(sorted(marks,reverse=True))

# list_mark = ','.join(str(i) for i in marks)
# print(list_mark)

# # видалення списку
# print(marks)
# del marks[0]
# print(marks)

# task 1

# number = input('number -->').split()
# sume = 0
# count = 0
# for i in number:
#     sume += int(i)
#     count += 1
# print('sume = ',sume)
# print('average',sume / count)

# number = input('number -->').split()
# number = [int(i) for i in number]
# print('sume = ',sum(number))
# print('average',sum(number) / len(number))

# task 2


# list = input('list --> ')
# a = input('enter -->')
# sun = 0
# for i in list:
#     if i == a:
#         sun += 1
# print(sun)


# task 3

# numbers = input('num --> ').split()
# sume = 0
# for i in numbers:
#     if int(i) > 0:
#         sume += int(i)
# print(sume)