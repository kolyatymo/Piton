# import re

# str_1 = '123'
# str_2 = '234'
# str_3 = 'lorem** 21 red ipsum red set hac'

# print('\n\n=================== re.search(template, str)=============')
# print(f'\t {str_1} \t\t\t --> {re.search('12', str_1)}')
# print(f'\t {str_2} \t\t\t --> {re.search('12', str_2)}')
# print(f'\t {str_3} \t--> {re.search('12', str_3)}')


# print('\n\n=================== re.search(template, str)=============')
# print(f'\t {str_1} \t\t\t --> {re.search('[12]', str_1)}')
# print(f'\t {str_2} \t\t\t --> {re.search('[12]', str_2)}')
# print(f'\t {str_3} \t--> {re.search('[12]', str_3)}')

# print('\n\n=================== re.search(template, str)=============')
# print(f'\t {str_1} \t\t\t --> {re.search('[0-9]', str_1)}')
# print(f'\t {str_2} \t\t\t --> {re.search('[0-9]', str_2)}')
# print(f'\t {str_3} \t--> {re.search('[0-9]', str_3)}')

# print('\n\n=================== re.search(template, str)=============')
# print(f'\t {str_1} \t\t\t --> {re.search('[a-zA-Zo-9]', str_1)}')
# print(f'\t {str_2} \t\t\t --> {re.search('[a-z]', str_2)}')
# print(f'\t {str_3} \t--> {re.search('[a-zA-Zo-9]', str_3)}')

# print('\n\n=================== re.search(template, str)=============')
# print(f'\t {str_1} \t\t\t --> {re.search('\w', str_1)}')
# print(f'\t {str_2} \t\t\t --> {re.search('\w', str_2)}')
# print(f'\t {str_3} \t--> {re.search('\w', str_3)}')

# match = re.search('[a-zA-Z]{3,10}\** \w+', str_3)
# if match:
#     print('find')
#     print(match.start(), match.end(), match.group(0))
# else:
#     print('not find')

# print('\n\n=================== re.search(template, str)=============')
# print(f'\t {str_1} \t\t\t --> {re.search('\w$', str_1)}')
# print(f'\t {str_2} \t\t\t --> {re.search('\w$', str_2)}')
# print(f'\t {str_3} \t--> {re.search('\w$', str_3)}')

# print('\n\n=================== re.search(template, str)=============')
# print(f'\t {str_1} \t\t\t --> {re.search('\w{3}$', str_1)}')
# print(f'\t {str_2} \t\t\t --> {re.search('\w{3}$', str_2)}')
# print(f'\t {str_3} \t--> {re.search('\w{3}$', str_3)}')

# # lower letters
# print('\n\n=================== re.search(template, str)=============')
# print(f'\t {str_1} \t\t\t --> {re.search('^\w{3}', str_1)}')
# print(f'\t {str_2} \t\t\t --> {re.search('^\w{3}', str_2)}')
# print(f'\t {str_3} \t--> {re.search('^\w{3}', str_3)}')

# # все крім що в []
# # {3} - три подрят
# # * - 0 - +
# # + - 1 - +
# print('\n\n=================== re.search(template, str)=============')
# print(f'\t {str_1} \t\t\t --> {re.search('^[a-z]{3}', str_1)}')
# print(f'\t {str_2} \t\t\t --> {re.search('^[a-z]{3}', str_2)}')
# print(f'\t {str_3} \t--> {re.search('^[a-z]', str_3)}')

# # те що відноситься до слова
# print('\n\n=================== re.search(template, str)=============')
# print(f'\t {str_1} \t\t\t --> {re.search('\W', str_1)}')
# print(f'\t {str_2} \t\t\t --> {re.search('\W', str_2)}')
# print(f'\t {str_3} \t--> {re.search('\W', str_3)}')

# # цифри
# print('\n\n=================== re.search(template, str)=============')
# print(f'\t {str_1} \t\t\t --> {re.search('\d*', str_1)}')
# print(f'\t {str_2} \t\t\t --> {re.search('\d*', str_2)}')
# print(f'\t {str_3} \t--> {re.search('\d*', str_3)}')

# # все крім цифри
# print('\n\n=================== re.search(template, str)=============')
# print(f"\t {str_1} \t\t\t --> {re.search('\D*', str_1)}")
# print(f"\t {str_2} \t\t\t --> {re.search('\D*', str_2)}")
# print(f"\t {str_3} \t--> {re.search('\D*', str_3)}")

# match = re.findall(r'red', str_3,count + 1)
# print(match)

# match = re.findall(r'[ .,]\w{3}[ .,]', str_3)
# print(match)

# for word in match:
#     print(word)

# # заміна слова
# # 1 - скільки слів замінити
# print(re.sub(r'[ .,]\w{3}[ .,]',' yellow ',str_3,count=1))

# print(f'{re.search(''),str_3}')

# import string
# import random

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.punctuation)

# print(",".join(random.sample(string.ascii_letters,8)))

# # tab = 20 symbol
# print('lorem'.center(50))
# print(' lorem '.center(50,'*'))
# print('\tlorem\t'.expandtabs(20))
# print('lorem'.rjust(20, '*'))
# print('lorem'.ljust(20, '*'))
# print('lorem'.rstrip('em'))
# print('lorem'.lstrip('lo'))
# print('mmlorem'.strip('m'))
# print('L124'.zfill(10))


# print('ttest {0:3.2f}'.format(2.3245235))
# print('ttest {0:4d}'.format(20))

# task 1

# user = input('line -->')
# print(len(user))

# task 2

# user = input('line -->')
# symbol = input('symbol -->')
# symbols = 0
# if len(symbol) != 1:
#     print('веддіть заново')
# else:
#     print
# for i in user:
#     if symbol == i:
#         symbols +=1
# print(symbols)

# task 3

# user = input('line -->')

# revers = ""
# for i in user:
#     revers = i + revers
# print(revers)


# print(user[::-1])

# task 4

# import re

# user = input('line -->')
# word = input('word -->')
# match = re.findall(word, user)
# print(len(match))

# task 5 
# import re
 
# user = input('line -->')
# word = input('word -->')
# replace = input('replace word -->')
# text = user.replace(word, replace, 1)
# print(text)

# task 6

# user = input('line -->')
# user1 = user.split()
# word = user[0]
# for i in user1:
#     if len(i) > len(word):
#         word = i
# print(i)