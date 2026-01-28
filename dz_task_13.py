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

# user = [random.randint(1,20) for i in range(10)]
# print(user)
# best_line = []
# start = [user[0]]
# for i in range(1, len(user)):
#     if user[i] > user[i-1]:
#         best_line.append(user[i])
#     else:
#         best_line = [user[i]]
#     if len(start) > len(best_line):
#         best_line = start
# print(len(best_line))
# print(best_line)


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

import random

user = [random.randint(1,20) for i in range(5)]
print(user)
result = []
min_ = user[0]
max_ = user[0]
for i in user:
    if min_ > i:
        min_ = i
    if max_ < i:
        max_ = i

    result.append(min_)


            
