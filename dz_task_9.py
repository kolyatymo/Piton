
# task 9


# img а
# q = 0
# while True:
#     pokaz = input('''

#         [a] --> малюнок a
#         [b] --> малюнок b
#         [i] --> малюнок i
#         [k] --> малюнок к
#         [g] --> малюнок г
#         [v] --> малюнок в
#         [0] --> stop 
#                             Enter --> ''')
#     if pokaz == '0':
#         break

#     line = 5
#     if pokaz == 'a':
#         for j in range(line,0,-1):
#             print(' ' * q, end='')
#             q += 2
#             for i in range(1, j+1):
#                 print('*', end=' ')
#             print()
#         print('--------- малюнок А ---------',)
# # img б

#     if pokaz == "b":
#         for i in range(1, line + 1):
#             print(" ",end=' ')
#             for j in range(1, i + 1):
#                 print('*', end=' ')
#             print()
#         print('--------- малюнок Б ---------',)
# # img і

#     if pokaz == "i":
#         for j in range(line,0,-1):
#             for i in range(1, j+1):
#                 print('*', end=' ')
#             print()
#         print('--------- малюнок І ---------',)


# # img к
 
#     if pokaz == "k":
#         for i in range(1, line + 1):
#             print(' ' * ((line - i)*2), end='')
#             for j in range(1, i+1):
#                 print('*', end=' ')
#             print() 
#         print('--------- малюнок К ---------',)


# # img г

#     if pokaz == "g":
#         for i in range(1, line + 1):
#             print(' ' * ((line - i)*2), end='')
#             for j in range(1, i+1):
#                 print('*', end=' ')
#             for j in range(i-1, 0,-1):
#                 print('*', end=' ')
#             print()
#         print('--------- малюнок Г ---------',)

# # img в
#     if pokaz == 'v':
#         for i in range(1, line +1):
#             print('*' * (line +1 - i)*2),
#             for j in range(1, i + 1):
#                 print(' ', end='')
#         print('--------- малюнок В ---------',)
    

