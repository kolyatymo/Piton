# for j in range(1,11):
#     for i in range(2,6):
#         print(f'{i} * {i} = {j * i}', end='\t')
# print()

# for j in range(1,11):
#     for i in range(6,10):
#         print(f'{i} * {i} = {j * i}', end='\t')


# flag = True


# num = int(input("number --> "))
# len = 0
# sum = 0
# zero = 0
# while True:
#     choice = int(input('''
#         [1] - кількість чисел
#         [2] - сума
#         [3] - серед
#         [4] - кількість нулів
#         [0] - error
#         --->'''))
        
#     if choice ==0:
#         break


#     while num !=0:
#         disigs = num % 10
#         num //= 10

#         len +=1
#         sum += disigs
#         if disigs ==0:
#             zero +=1


#     match choice:
#         case 1:
#             print(len)
#         case 2:
#             print(sum) 
#         case 3:
#             print(sum / len)
#         case 4:
#             print(zero)


'''
1
12
123
1234
12345

'''
# for i in range(1,2):
#     print(i, end=' ')
# print()

# for i in range(1,3):
#     print(i, end=' ')
# print()

# for i in range(1,4):
#     print(i, end=' ')
# print()

# print ('1')
# print('1 2')
# print('1 2 3')
# print('1 2 3 4')
# print('1 2 3 4 5')

# line = int(input('number : ')) 
# for j in range(1, line+1):
#     for i in range(1, j+1):
#         print(i,end=' ')
#     print()

# line = 5

# # for i in range(1, line+1):
# #     print(i, end=' ')
# # print()  

# # for i in range(1, line):
# #     print(i, end=' ')
# # print()    
# q = 0
# for j in range(line, 0, -1):
#     print(' '*q,end='')
#     q+=2
#     for i in range(1, j +1):
#         print(i, end=' ')
#     print() 

line = 4

# '''
#       1
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1

# '''

# print(" " * 3 * 2, end='')
# print('1', end=' ')
# print()

# print(" " * 2 * 2, end='')
# print('1', end=' ')
# print('2', end=' ')
# print('1', end=' ')
# print()

# print(" " * 1 * 2, end='')
# print('1', end=' ')
# print('2', end=' ')
# print('3', end=' ')
# print('2', end=' ')
# print('1', end=' ')
# print()

# print(" " * 0 * 2, end='')
# print('1', end=' ')
# print('2', end=' ')
# print('3', end=' ')
# print('4', end=' ')
# print('3', end=' ')
# print('2', end=' ')
# print('1', end=' ')
# print()

# for i in range(1, line + 1):
#     print(' ' * ((line - i)*2), end='')
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()    

# for i in range(1, line + 1):
#     print(' ' * ((line - i)*2), end='')
#     for j in range(1, i+1):
#         print(j, end=' ')
#     for j in range(i-1, 0,-1):
#         print(j, end=' ')
#     print()  


# task 1
# start = int(input('number_1 --> '))
# end = int(input('number_2 --> '))
# for i in range(1, end+1):
#     print(f'Дільники для числа {i}','-',end=' ')
#     for j in range(1, i +1):
#         if i % j ==0:
#             print(j, end=' ')
#     print()

# task 2
# for i in range(3, 1000+1):
#     sum = 0
#     for j in range(1, i+1):
#         if i % j ==0:
#             sum+=1
#     if sum ==2:
#         print(i)


# task 3
# sum = 0
# for i in range(10):
#     for j in range(10):
#         for q in range(10):
#             if i != j and i != q and j != q:
#                 print(i,j,q)
#                 sum+=1
# print('кількість комбінацій --> ', sum)
# print('кількість секунд --> ', sum * 3)              

