'''
5! = 5 * 4!
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1!
1! = 1
0! = 1

'''

# def factor(number):
#     if number == 1 or number == 0:
#         return number
#     return number * factor(number - 1)

# print(factor(5))

'''
2^4 --> 2 * 2^3
2^3 --> 2 * 2^2
2^2 --> 2 * 2^1
2^1 --> 2
'''
# def power(number, step):
#     if step == 1:
#         return number
#     return number * power(number,step - 1)

# print(power(2,4))

'''
1234 --> 4 + sume(123)
123 --> 3 + sume(12)
12 --> 2 + sume(1)
1 --> 1 + sume(0)
0 --> 0
'''

# def sume_(number):
#     if number < 10:
#         return number
#     return number % 10 + sume_(number // 10)
# print(sume_(9657))

# def max_(num):
#     if num < 10:
#         return num
#     return num % 10 if num % 10 > max_(num // 10) else max_(num // 10)  
# print(max_(9867))


# def sume_(number, sum = 0):
#     if number == 0:
#         return sum
#     sum += number % 10
#     return sume_(number // 10, sum)

# print(sume_(9524))

'''
1 2 3 4 5
'''

# def numbers_(a,b):
#     if b < a: return 
#     print(b) 
#     numbers_(a ,b - 1)

# numbers_(1,10)

# def numbers_(a,b):
#     if a > b: return 
#     print(a) 
#     numbers_(a+1,b)

# numbers_(1,10)


'''
1234 - 4321
'''

# def palindrom(number, sume = 0):І
#     if number == 0:
#         return sume
#     return palindrom(number // 10, sume * 10 + number % 10)

# # print(palindrom(1234))

# def breath(number):
#     if number == 0:
#         return
#     print('(',end='')
#     breath(number - 1)
#     print(')',end='')

# print(breath(3))

# # task 1

# def num(a):
#     return max(str(a))
# print(num(1234967))

# # task 2

# def proste(a):
#     if a < 2:
#         return False
#     for i in range(2,a):
#         if a % i == 0:
#             return a, 'не є простим'
# print(proste(7))

# task 3

# def mnoznuki(a):


