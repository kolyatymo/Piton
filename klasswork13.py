# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix[0][2])


# m = [
#     [
#         [1,2,3],
#         [4,5,6]
#     ],
#     [
#          [7,8,9],
#         [8,9,5]
#     ],
# ]
# print(m[0][1][2])

# for i in m:
#     for j in i:
#         for h in j:
#             print(h, end='\t')
#         print()
#     print()


# for row in matrix:
#     for j in row:
#         print(j,end='\t')
#     print() 

import random

# matrix = []

# for i in range(3):
#     row = []
#     for j in range(5):
#         row.append(random.randint(1,20))
#     matrix.append(row)

# matrix = [[random.randint(1,20) for i in range(5)] for j in range(3)]

# for row in matrix:
#     for data in row:
#         print(data,end='\t')
#     print()

# sum_ = 0
# # for row in matrix:
# #     sum_ += sum(row)
# # for row in matrix:
# #     for data in row:
# #         sum += data
# print(sum_,'sum')

# min_ = matrix[0][0]
# max_ = matrix[0][0]

# for row in matrix:
#     for data in row:
#         if min_ > data:
#             min_ = data
#         if max_ < data:
#             max_ = data

# for row in matrix:
#     if min_ > min(row):
#         min_ = min(row)
#     if max_ < max(row):
#         max_ = max(row)

# min_ = []
# max_ = []

# for row in matrix:
#     min_.append(min(row))
#     max_.append(max(row))


# print(min(min_),'  min')
# print(max(max_),' max')


# min_ = min([min(row) for row in matrix])
# max_ = max([max(row) for row in matrix])

# print(min_,'  min')
# print(max_,' max')


# min_ = matrix[0][0]
# max_ = matrix[0][0]
# min_col = 0
# min_row = 0
# max_col = 0
# max_row = 0

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if min_ > matrix[i][j]:
#             min_ = matrix[i][j]
#             min_row = i
#             min_col = j
#         if max_ < matrix[i][j]:
#             max_ = matrix[i][j]
#             max_row = i
#             max_col = j

# print(f'Max --> {max_}[{max_row},{max_col}]')
# print(f'Min --> {min_}[{min_row},{min_col}]')


# matrix = [[random.randint(1,20) for i in range(5)] for j in range(3)]
# clone = matrix.copy()
# for i in range(len(clone)):
#     clone[i] = matrix[i].copy()
# clone[0][0] = 333
# print('orig')
# for row in matrix:
#     for data in row:
#         print(data,end='\t')
#     print()
# print()

# print('clone')
# for row in clone:
#     for data in row:
#         print(data,end='\t')
#     print()
# print()



# task 1

# import random

# a = []

# for i in range(10):
#     a.append(random.randint(1,20))

# print(a)

# min_ = a[0]
# max_ = a[0]
# for i in a:
#     if i < min_:
#         min_ = i
#     if i > max_:
#         max_ = i
# print(max_)
# print(min_)
# min_index = a.index(min_)
# max_index = a.index(max_)
# for i in range(min(min_index, max_index) + 1, max(min_index, max_index)):
#     a[i] *=2
# print(a)



# task 2


# a = []
# for i in range(10):
#     a.append(random.randint(1,20))
# print(a)

# for i in range(0, row -1,2):
#     print(a[i])

# task 3

#
# a = []
# for i in range(11):
#     a.append(random.randint(1,20))
# print(a)

# for i in range(len(a)):
#     count = 0
#     for j in range(len(a)):
#         if a[i]==a[j]:
#             print(a)


# task 4


# import random

# a = []

# for i in range(3):
#     row = []
#     for j in range(4):
#         row.append(random.randint(1,20))
#     a.append(row)

# row_sum = []
# for i in range(3):
#     sume = 0
#     for j in range(4):
#         sume += a[i][j]
#     row_sum.append(sume)

# col_sume = []
# for j in range(4):
#     sume1 = 0
#     for i in range(3):
#         sume1 += a[i][j]
#     col_sume.append(sume1)

# sum_ = 0
# for i in range(3):
#     for j in range(4):
#         sum_ += a[i][j]


# for i in range(3):
#     print(i+1,'-->',row_sum)

# for j in range(4):
#     print(j+1,'-->',col_sume)

# print('sume -->',sum_)
