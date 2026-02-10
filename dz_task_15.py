
# task 1

# def max_(number):
#     if number < 10:
#         return number
#     return number % 10 if number % 10 > max_(number // 10) else max_(number // 10)
# print(max_(756498))

# task 2

# def prime(number, i=2):
#     if number <= 1:
#         return False
#     if i > number // 2:
#         return True
#     if number % i == 0:
#         return False
#     return prime(number, i + 1)

# print(prime(1244))


# task 3

# def dividers(number, i = 2):
#     if number == 1:
#         return
#     if number % i == 0:
#         print(i)
#         dividers(number // i)
#     else:
#         dividers(number, i + 1)
# print(dividers(18))
        
# task 4

# def fibonaci(number):
#     if number == 1 or number == 2:
#         return number
#     return fibonaci(number-1) + fibonaci(number-2)
# print(fibonaci(10))