# Напишіть програму, яка запитує в користувача три рядки і 
# записує їх у файл data.txt, кожен рядок має бути записаний на новому рядку

# task 1

# user = input('line --> ')
# user1 = input('line --> ')
# user2 = input('line --> ')
# with open(r'files/data.txt', 'w') as file:
#     file.write(f'{user}\n{user1}\n{user2}\n')

# task 1   №2

# with open('files/nagib.txt', 'w') as line:
#     for i in range(3):
#         text = input(f'text --> {i + 1}: ')
#         line.write(text + '\n')

# task 2

# directory = 'files'
# file_in = 'data.txt'

# with open(f'{directory}/{file_in}') as file:
#     line = file.readlines()
    
# for i in range(1, len(line), 2):
#     print(line[i],end='')

# task 3


# directory = 'files'
# file_in = 'data.txt'
# file_out = 'filtered.txt'

# with open(f'{directory}/{file_in}') as file:
#     text = file.read().split()


# with open(f'{directory}/{file_out}','w') as line:
#     for i in text:
#         if i == 'Python':
#             line.write(i + '\n')

# task 4

# directory = 'files'
# file_out = 'cleaned.txt'
# name = input('name-->')

# with open(f'{directory}/{name}') as file:
#     text = file.read().split()

# res = ''
# for i in text:
#     if not i.isdigit():
#         res += i

# with open(f'{directory}/{file_out}','w') as line:
#     line.write(res)

# task 5


# directory = 'files'
# file_in = 'log.txt'
# file_out = 'word_stats.txt'

# with open(f'{directory}/{file_in}') as file:
#     text = file.read().split()

# res = {}
# for i in text:
#     if i not in res:
#         res[i] = 0
#     res[i] += 1

# with open(f'{directory}/{file_out}','w') as line:
#     for i in res:
#         line.write(i + ' ' + str(res[i]) + ' ' + '\n')
        
# directory = 'files'
# file_in = 'log.txt'
# file_out = 'word_stats.txt'

# with open(f'{directory}/{file_in}') as f:
#     words = f.read().split()

# counts = {}

# for w in words:
#     if w not in counts:
#         counts[w] = 0
#     counts[w] += 1

# with open(f'{directory}/{file_out}', 'w') as f:
#     i = 0
#     for word in counts:
#         f.write(word + ' ' + str(counts[word]) + '\n')
#         i += 1
#         if i == 10:
#             break


# task 6

# directory = 'files'
# file_in = 'data1.txt'
# file_out = 'reversed.txt'

# with open(f'{directory}/{file_in}') as file:
#     all_text = file.readlines()
    
# # print(all_text)
# print(all_text[::-1])

# if '\n' not in all_text[-1]:
#     all_text[-1] += '\n'


# with open(f'{directory}/{file_out}','w') as file:
#     file.writelines(all_text[::-1])



