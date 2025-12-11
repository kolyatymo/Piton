
# task 1
# number = int(input('number enter : '))
# number2 = int(input('number enter : '))
# number3 = int(input('number enter : '))
# sum_product = input('sum and product : ')
# if sum_product == 'sum':
#     sum = number + number2 + number3
#     print(sum)
# elif sum_product == 'product':
#     product = number * number2 * number3
#     print(product)

# task 2
# number = int(input('number enter : '))
# number2 = int(input('number enter : '))
# number3 = int(input('number enter : '))
# max_min_midl = input('max or min or midl : ')
# if max_min_midl == 'max':
#     if number > number2 and number > number3:
#         print(number)
#     elif number2 > number3 and number2 > number:
#         print(number2)    
#     else:
#         print(number3)
# if max_min_midl == 'min':
#     if number < number2 and number < number3:
#         print(number)
#     elif number2 < number3 and number2 < number:
#         print(number2)    
#     else:
#         print(number3)
# if max_min_midl == 'midl':
#     print((number + number2 + number3)/3)       

# task 3
# number = input('number : ')
# if number == '1':
#     print('Дуже погано')
# elif number == '2':
#     print('Погано')
# elif number == '3':
#     print('Задовільно')
# elif number == '4':
#     print('Добре')
# elif number == '5':
#     print('Відмінно')    

# task 4
# meters = int(input('meters : '))
# variant = input('muli, duim, jardu. all together. km cm : ')
# if variant == 'muli':
#     muli = meters * 0.00062
#     print('muli : ',muli)
# elif variant == 'duim':
#     duim = meters * 39
#     print('duim : ',duim)    
# elif variant == 'jardu':
#     jardu = meters * 1.09
#     print('jardu : ', jardu)
# elif variant == 'all together':
#     muli = meters * 0.00062
#     duim = meters * 39
#     jardu = meters * 1.09
#     print('muli : ',muli, 'duimu : ',duim, 'jardu : ',jardu)
# elif variant == 'km cm':
#     km = meters * 1000
#     cm = meters / 100
#     print(km, cm)

# task 5
# number1 = int(input('number 1 : '))
# number2 = int(input('number 2 : '))
# operathija = input('+, -, *, /, %, **,')
# if operathija == '+':
#     sum = number1 + number2
#     print(sum)
# elif operathija == '-':
#     sum = number1 - number2
#     print(sum)
# elif operathija == '*':
#     sum = number1 * number2
#     print(sum) 
# elif operathija == '/':
#     sum = number1 / number2
#     print(sum)  
# elif operathija == '%':
#     sum = number1 % number2
#     print(sum) 
# elif operathija == '**':
#     sum = number1 ** number2
#     print(sum)           

# task 6
# number = int(input('numeric : '))
# num1 = number // 100 % 10
# num2 = number // 10 % 10
# num3 = number % 10
# if num1 == num2 and num1 == num3:
#     print('Всі цифри однакові')
# else:
#     print('Цифри різні')