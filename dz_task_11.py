# task 1

# import re
# text = 'samply dummay of thea priatiag typesetting industry Lorem Ipsum has beon toe inoustrys stoandoard duommoy evoer sinoce'

# a = re.sub('a', '*',text,5)
# b = re.sub('o', '-',a[::-1],7)[::-1]
# print(b)

# task 2

# password = input('password -->')
# upper = 0
# lower = 0
# digit = 0
# for i in password:
#     if i.isupper():
#         upper += 1
#     elif i.islower():
#         lower += 1
#     elif i.isdigit():
#         digit += 1

# if len(password) < 6:
#     print('пароль має містити більше 6 символів')
# elif upper == 0:
#     print('пароль має містити хоч 1 велику літеру')
# elif lower == 0:
#     print('пароль має містити хоч 1 маленьку літеру')
# elif digit == 0:
#     print('пароль має містити хоч 1 цифру')
# else:
#     print(password, ' -->  пароль вірний')

# task 3

# text = 'У ясну літню пору я іду у ліс, де є пташиний спів і юний шум дерев.'
# vowels = 'аеєиіїоуюя'
# count = 0

# for i in text:
#     if i in vowels:
#         count +=1
# print('в тексті',count, 'голосних')

# task 4

# text = 'shabucu ash uu asuh uas usu h'
# lenn = 20
# if len(text) > lenn:
#     text = text[:lenn-1] + '...'
# print(text)

# task 5

# text = 'more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum'
# text1 = text.split()
# count = 0
# word = 0
# for i in text1:
#     word += len(i)
#     count +=1
# print('середня довжина слів', word // count)

# task 6

# text = 'ACA123recently'
# text1 = ''
# for i in text:
#     if i.islower():
#         text1 += i.upper()
#     elif i.upper():
#         text1 += i.lower()
#     elif i.isdigit():
#         text1 += '-'
#     else:
#         text1 += i
# print(text1)