'''

1 - open file
2 - read file
3 - write file
4 - close file

'''


# ------------ read ------------

# url = r'C:\Users\Vlad\Desktop\test.txt.txt'

# fileHandler = open(url)
# print(type(fileHandler), fileHandler)
# text = fileHandler.read()
# print(text, type(text), sep='\n')
# print('Position file curcore' ,fileHandler.tell())
# fileHandler.close()

# fileHandler = open(url)
# test = fileHandler.read(15)
# print(test)

# print('Position file curcore' ,fileHandler.tell())
# fileHandler.seek(0)

# text = fileHandler.readline()
# print('read line -->', text)

# fileHandler.seek(0)
# for line in fileHandler:
#     print(line)

# fileHandler.seek(0)

# text = fileHandler.readlines()
# print()
# print(text)
# print(text[-1])
# fileHandler.close()


# with open(url) as file:
#     print(file.read())


#----------------------- write file ----------

# with open(r'files/my_file.txt', 'w') as file:
#     file.write('Hello World')

# with open(r'files/my_file.txt', 'a') as file:
#     file.write('Hello World 3 \n')

# with open(r'files/my_file_ua.txt', 'a', encoding='utf-8') as file:
#     file.write('Привіт світ 1\n')

# with open(r'files/my_file_ua.txt', 'r', encoding='utf-8') as file:
#     print(file.read())

#----------------- practical --------------

#task 1

# with open(r'files/output.txt', 'w') as file:
#     file.write('Hello World!')

# task 2

# with open(r'files/output.txt', 'r') as file:
#     print(file.read())

# task 3

url = r'C:\Users\Vlad\Desktop\data.txt'

# text = open(url)
# line = text.read()

# with open(r'files/output.txt', 'w') as file:
#     file.write(line)

# task 4

# text = open(url)
# file = text.read()

# line_1 = text.readlines()
# print(line_1)

# lines = file.count('\n')
# print(lines)

# task 5

text = open(url)



line = text.read()
lines = text.readlines()
line1 = line.split()

line3 = len(lines)
word1 = len(line)
line2 = len(line1)


with open(r'files/summary.txt', 'w') as file:
    file.write(line3)
    file.write(word1)
    file.write(line2)

# task 6

# text = open(url)
# line = text.read()
# print(line)
# print()
# res = ''
# for i in line:
#     if i =='z':
#         res += 'a'
#     elif i == 'Z':
#         res += 'A'
#     elif 'a' < i < 'z':
#         res += chr(ord(i) + 1)
#     else:
#         res += i
# with open(r'files/encrypted.txt' , 'w') as file:
#     file.write(res)
        
