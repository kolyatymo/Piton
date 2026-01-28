# task 1

# import random
# a = []
# for i in range(10):
#     a.append(random.randint(1,20))

# print(a)

# min_ = a[0]
# max_ = a[0]
# for i in a:
#     if min_ > i:
#         min_ = i
#     if max_ < i:
#         max_ = i
# print('Min --> ',min_)
# print('Max --> ',max_)

# min_index = a.index(min_)
# max_index = a.index(max_)
# for i in range(min(min_index, max_index)+1, max(min_index, max_index)):
#     a[i] *= 2
# print(a)

# for j in range(len(a)):
#     if a[j] != min_ and a[j] != max_:
#         a[j] *= 2
# print(a)


# task 2

# import random
# a = []
# for i in range(10):
#     a.append(random.randint(1,20))
# print(a)

# b = []
# for i in range(1,10,2):
#     b.append(a[i])
# print(b)
    
# task 3

# import random

# a = []
# for i in range(10):
#     a.append(random.randint(1,20))
# print(a)
# count = []
# for i in a:
#     if a.count(i) > 1 and i not in count:
#         count.append(i)
# print(count)

# task 4

# import random
# a = []
# for i in range(3):
#     row = []
#     for j in range(4):
#         row.append(random.randint(1,20))
#     a.append(row)

# for row in a:
#     for q in row:
#         print(q,end='\t')
#     print()
# print()

# row_count = []
# for i in range(3):
#     sume = 0
#     for j in range(4):
#         sume += a[0][j]
# print('сума строки 1 --> ',sume)
# print()

# row_count = []
# for i in range(3):
#     sume = 0
#     for j in range(4):
#         sume += a[1][j]
# print('сума строки 2 --> ',sume)
# print()

# row_count = []
# for i in range(3):
#     sume = 0
#     for j in range(4):
#         sume += a[2][j]
# print('сума строки 3 --> ',sume)
# print()

# col_count = []
# for j in range(4):
#     count = 0
#     for i in range(3):
#         count += a[i][0]
# print('сума стовбця 1 --> ',count)
# print()

# col_count = []
# for j in range(4):
#     count = 0
#     for i in range(3):
#         count += a[i][1]
# print('сума стовбця 2 --> ',count)
# print()

# col_count = []
# for j in range(4):
#     count = 0
#     for i in range(3):
#         count += a[i][2]
# print('сума стовбця 3 --> ',count)
# print()

# col_count = []
# for j in range(4):
#     count = 0
#     for i in range(3):
#         count += a[i][3]
# print('сума стовбця 4 --> ',count)
# print()

# sumee = 0
# for i in range(3):
#     for j in range(4):
#         sumee += a[i][j]
# print('загальна сума --> ',sumee)    