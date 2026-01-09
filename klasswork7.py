
# "text for"

# i = 1
# for letter in "text for":
#     print(letter * i)
#     i += 1

# print(range(10)) # 0 1 2 3 ... 9

# for i in range(10):
#     print(i, end='\t')
# print()

# for i in range(1, 10): # 1 2 3 ... 9
#     print(i, end='\t')
# print()

# for i in range(1, 10, 2):
#     print(i, end='\t')
# print() # 1 3 5 7 9 

# for i in range(10, 1, -2):
#     print(i, end='\t')
# print()

# number = int(input('num : ')) # 5 {1 2 3 4 5}

# for i in range(1, number + 1):
#     if number % i == 0:
#         print(i, end="\t")


# number 1
# number = int(input('num : '))
# counter = 0

# for i in range(1, number+1):
#     if number % i == 0:
#         counter+=1
        
# if counter == 2:
#     print("prime")
# else:
#     print('складне')


# n umber 2
# number = int(input('num : '))
# Flag = True
# for i in range(2, number):
#     if number % i == 0:
#         Flag = False
#         break

# if Flag:
#     print('prime')
# else:
#     print('complex')

# number 3
# number = int(input('num : '))
# for i in range(2, number // 2 + 1):
#     if number % i == 0:
#         print('complex')
#         break
# else:
#     print('prime')



# к м н!!!

# import random

# # for i in range(5):
# #     # print(random.random(1, 10))
# #     print(random.choice('rps'))
# user_counter = 0
# bot_counter = 0
# draw_counter = 0
# while True:
#  levels = 0
#  bot_score = 0
#  user_score = 0
#  while levels < 3:
#      levels+=1
#      print(f'----------------------round #{levels}---------------------')
#      while True:
#          user = input('''
#                       [s] - scrissors 
#                       [p] - paper 
#                       [r] - rock 
#                       enter : ''')
#          if user =='s' or user == 'p' or user == 'r':
#              break
#          else:
#              print('error')
#      bot = random.choice('srp')

#      print(f''' 
#          user    Bot
#          [{user}]      [{bot}]
#            ''')
#      if user == 's' and bot == 'p' or user == 'p' and bot == 'r' or user == 'r' and bot == 's':
#          user_score +=1
#      elif bot == user:
#          continue
#      else:
#          bot_score +=1
#  if user_score > bot_score:
#      print('------------usser win!!!-------------')
#      user_counter+=1
#  elif user_score == bot_score:
#      print('============draw!!!==============')
#      draw_counter+=1
#  else:
#      print('------------loser!!!-------------')
#      bot_counter+=1

#  while True:
#   way = input('restart [y] - yes; [n] - no : ')
#   if way == 'y' or way == 'n':
#       break  
#   else:
#       print('error! choise')   
#  if way == 'n': 
#     break

# print(f'''
#             [user win] -- {user_counter}
#             [bot win] -- {bot_counter}
#             [draw] -- {draw_counter}
# ''')