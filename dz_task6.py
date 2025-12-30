# task 1
# num1 = int(input("number 1 : "))
# num2 = int(input("number 2 : "))
# i = num1
# while i <= num2:
#     if i % 7 == 0:
#      print(i, end="\t")
#     i+=1

# task 2
# start = int(input("number 1 : "))
# end = int(input("number 2 : "))
# print("весь діапазон")
# i = start
# while i <= end:
#     print(i, end='\t')
#     i += 1
# print('\n')

# print("діапазон спадання")
# i = end
# while i >= start:
#     print(i, end='\t')
#     i -= 1
# print('\n')

# print('кратні 7')
# i = start
# while i <= end:
#     if i % 7 ==0:
#         print(i, end='\t')
#     i += 1
# print('\n')        

# print('кількість чисел кратних 5')
# sum = 0
# i = start
# while i <= end:
#     if i % 5 ==0:
#         sum += 1
#     i += 1    
# print(sum, end="\t")

# task 3
# start = int(input("number 1 : "))
# end = int(input("number 2 : "))
# i = start
# while i <= end:
#     if i % 3 == 0 and i % 5 == 0:
#         print('Fizz Buzz')
#     elif i % 3 == 0:
#         print("Fizz")   
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)
#     i += 1

# task 4
# start = int(input("number 1 : "))
# end = int(input("number 2 : "))
# krok = int(input("krok : "))
# pramo_zworot = input("pramo, zworot : ")
# i = start
# if pramo_zworot == 'pramo':
#     while i <= end:
#         print(i)
#         i += krok
# elif pramo_zworot == 'zworot':
#     i = end
#     while i >= start:
#         print(i)     
#         i -= krok



# task 5
# num1 = int(input("number 1 : "))
# num2 = int(input("number 2 : "))
# if num1 > num2:
#  num1, num2 = num2, num1
 
# dobytok = 1
# i = num1
# while i <= num2:
#     if i % 4 == 0 and i % 6 !=0:
#         dobytok *= i 
#     i += 1
# if dobytok ==1:
#    print("Error")

# print(dobytok)

# task 2 №2
# start = int(input("number 1 : "))
# end = int(input("number 2 : "))
# i = start
# a = start
# b = end
# sum = 0
# h = start
# while i <= end:
#     i += 1
#     print(i)
# while b >= start:
#     b -= 1
#     print(b)
# while a <= end:
#     a += 1
#     if a % 7 ==0:
#         print("Числа кратні 7 : ",a)
# while h <= end:
#     if h % 5 ==0:
#         sum += 1
#     h += 1    
# print('Кількість чисел кратних 5 : ',sum)
# start = int(input("number 1 : "))
# end = int(input("number 2 : "))
# krok = int(input("krok : "))
# pramo_zworot = input("pramo, zworot : ")
# i = start
# while i <= end:
#     if pramo_zworot == 'pramo':
#         print(i)
#         i += krok
# i = end        
# while i >= start:
#     if pramo_zworot == 'zworot':
#         print(i)     
#         i -= krok

# task 4 №2
# start = int(input("number 1 : "))
# end = int(input("number 2 : "))
# krok = int(input("krok : "))
# pramo_zworot = input("pramo, zworot : ")

# if krok <=0:
#     print('fdsfsdf')
# else:
#     if pramo_zworot == 'pramo':
#         i = start
#         while i <= end:
#             print(i)
#             i += krok

#     elif pramo_zworot == 'zworot':
#         i = end
#         while i >= start:
#             print(i)
#             i -= krok
#     else:
#         print('error')