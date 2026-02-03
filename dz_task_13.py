# task 1

# import random
# user = [random.randint(1,20) for i in range(10)]
# count = 0
# print(user)
# print()
# for i in range(1, len(user)):
#     if user[i] > user[i-1]:
#         count+=1
# print(count)


# task 2

# import random

# resul = []

# user = [random.randint(1,20) for i in range(10)]
# print(user)
# for i in user:
#     if user.count(i) == 1:
#         resul.append(i) 
# print(resul)

# task 3


# import random

# number = [random.randint(1,10) for i in range(10)]
# print(number,'\n')
# result = []
# start = [number[0]]
# for i in range(1, len(number)):
#     if number[i] > number[i - 1]:
#         start.append(number[i])
#     else:
#         if len(start) > len(result):
#             result = start
#         start = [number[i]]
# print(result,'\n \n',len(result))


# task 4

# import random

# user = [random.randint(1,20) for i in range(10)]
# print(user)
# a = []
# n = random.randint(3,6)
# print(n)
# for i in range(n):
#     last = user.pop()
#     user.insert(0,last)
# print(user)

# task 5

# import random

# user1 = [random.randint(1,20) for i in range(5)]
# user2 = [random.randint(1,20) for i in range(5)]
# print('line one --> ',user1)
# print('line two --> ',user2)
# print()
# user3 = user1 + user2
# print('line 3',user3)
# print()
# user_duplicate = list(set(user1 + user2))
# print('duplicate - line 1 and 2 --> ',user_duplicate)
# print()
# user4 = []
# for i in user1:
#     if i in user2 and i not in user4:
#         user4.append(i)
# print('спільні елементи --> ',user4)
# print()
# user5 = []
# for i in user1:
#     if i not in user2:
#         user5.append(i)
# for i in user2:
#     if i not in user1:
#         user5.append(i)
# print('різні елементи --> ',user5)
# print()
# user_min_max_line_1 = [min(user1), max(user1)]
# print('мін та макс першого списку --> ',user_min_max_line_1)
# user_min_max_line_2 = [min(user2), max(user2)]
# print('мін та макс другого списку --> ',user_min_max_line_2)

# task 6

# import random

# user = [random.randint(1,20) for i in range(4)]
# print(user)
# result = []
# user.sort()
# min_ = 0
# max_ = len(user)-1
# for i in range(len(user)):
#     if i % 2 == 0:
#         result.append(user[min_])
#         min_+=1
#     else:
#         result.append(user[max_])
#         max_-=1
# print(result)