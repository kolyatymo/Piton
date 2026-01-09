# task 1 !!!!
# num1 = int(input('num1 : '))
# num2 = int(input('num2 : '))
# parni=0
# neparni=0
# kratni9=0
# for i in range(num1 +1, num2 +1):
#     if i % 2 == 0:
#         parni+=i
#         print('parni : ',parni, end='\t')

#         print('\n')        
#     if i % 2 != 0:
#         neparni+=i
#         print('neparni : ',neparni, end='\t')

#     if i % 9 == 0:
#         kratni9+=i
#         print('kratni 9 : ',kratni9, end='\t')

# print('SEREDNE',parni + neparni + kratni9 / 3)

# task 2
# dowshuna = int(input('dowshuna : '))
# sumvol = input('sumvol : ')
# for i in range(1, dowshuna+1):
#     print(sumvol)

# task 3
# while True:
#  user = int(input('num1 : '))
#  if user == 7:
#      break
#  elif user > 0: 
#      print('Number is positive')
#  elif user < 0: 
#      print('Number is negative')
#  elif user ==0:
#      print('Number is equal to zero')
# print('Doog bye!')  


# task 4 !!!!

# sum = 0
# max = None
# min = None

# while True:
#     user = int(input('number --> '))

#     if user == 7:
#         print('Good bye!')
#         break
#     sum += user

#     if min == None:
#         min = user
#         continue

#     if max == None:
#         max = user
#         continue

#     if min > user:
#         min = user
#     if max < user:
#         max = user

# print('sum -->', sum)
# print('min -->', min)
# print('max -->', max)


# task 5 !!!!
# while True:
#  user = int(input('number --> '))
#  for i in range(2, user // 2 + 1):
#      if user % i == 0:
#          print('Число',user,'не є простим')
#          break
#  else:
#      print('Число',user,'є простим') 
#      if user <= 1:
#         break   
# print('Число має бути більшим за 1')

# task 6  

# user = int(input('num : '))
# a,b = 0,1
# while a <= user:
#     if a == user:
#         print(f'Число {user} належить послідовності фібоначчі')
#         break
#     a,b = b, a + b
# else:
#     print(f'Число {user} не належить послідовності фібоначчі')  