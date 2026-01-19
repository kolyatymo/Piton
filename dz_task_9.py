
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
#         [d] --> малюнок д
#         [e] --> малюнок е
#         [z] --> малюнок з
#         [j] --> малюнок ж
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
#         line = 11
#         for i in range(1, line +1):
#             line -= 2
#             print('*' * line, end=' ')
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

# # # img в
#     if pokaz == 'v':
#         q = 11
#         line = 5
#         for i in range(1, line +1):
#             q -= 2
#             print(' ' * i, end='')
#             print('*' * q, end='')
#             print(' ' * i, end='')
#             print()
#         print('--------- малюнок В ---------',)
    

#     # img д
#     if pokaz == 'd':
#         line = 11
#         q = 5
#         for i in range(1, line +1):
#             q -= 2
#             print(' ' * i, end='')
#             print('*' * line, end='')
#             print(' ' * i, end='')
#             print()

#         for i in range(4, 0, -1):
#             q += 2
#             print(' ' * i, end='')
#             print('*' * line, end='')
#             print(' ' * i, end='')
#             print()
#         print('--------- малюнок Д ---------',)
    
#     # img e
#     if pokaz == 'e':
#         q = 10
#         line = 5
#         for i in range(1, line +1):
#             q -= 2
#             print('*' * i, end='')
#             print(' ' * q, end='')
#             print('*' * i, end='')
#             print()


#         for i in range(4, 0, -1):
#             q += 2
#             print('*' * i, end='')
#             print(' ' * q, end='')
#             print('*' * i, end='')
#             print()
#         print('--------- малюнок Е ---------',)


#     # img ж
#     if pokaz == 'j':
#         line = 10
#         star = 0
#         space = line
#         flag = True
#         for i in range(1, line):
#             if flag:
#                 star += 1
#                 space-=2
#             else:
#                 star -=1
#                 space +=2
#             if star == line // 2:
#                 flag = False
#             print('*' * star, end='')
#             print(' ' * space, end='')
#             print()
#         print('--------- малюнок Ж ---------',)

#     # img з
#     if pokaz == 'z':
        # line = 10
        # star = 0
        # space = line
        # flag = True
        # for i in range(1, line):
        #     if flag:
        #         space -=1
        #         star +=1
        #     else:
        #         space +=1
        #         star -=1
        #     if star == line // 2:
        #         flag = False
        #     print(' ' * space, end='')
        #     print('*' * star, end='')
        #     print()
#         print('--------- малюнок З ---------',)


        