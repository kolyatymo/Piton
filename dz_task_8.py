# task 1

# x = int(input('number_x_ --> '))
# y = int(input('number_y_ --> '))
# sum = 1
# i = 0
# while i < y:
#     sum *= x
#     i+=1
# print(sum)    


# result = x ** y
# print(result)

# task 2

# number = int(input('number --> '))
# sum = 0
# print(f'дільники числа {number}','-', end=' ') 
# for i in range(1, number+1):
#     if number % i ==0:
#         print(i, end=' ')        
#         sum+=1
# print()
# print("Кількість дільників --> ",sum)

# # task 3
# sum = 0
# for i in range(100, 1000):
#     q = i // 100
#     w = (i // 10) - q * 10
#     e = i % 10
#     if q == w or q == e or w == e:
#         sum+=1
# print(sum)

# 234  1  -  2; 2  -  

# task 4 
# sum = 0
# for i in range(100, 1000):
#     q = i // 100
#     w = (i // 10) % 10
#     e = i % 10
#     if q != w and q != e and w != e:
#         sum += 1
# print(sum)  

# task 5
# start = int(input('number_1 --> '))
# end = int(input('number_2 --> '))
# for i in range(start, end+1):
#     sum = 0
#     for j in range(1, i):
#         if i % j ==0:
#             sum += j
#     if sum == i:        
#             print(i)

# task 6

# number = input('number --> ')
# result = ''
# for i in number:
#     if i != '3' and i != '6':
#         result += i 
# print(result)

