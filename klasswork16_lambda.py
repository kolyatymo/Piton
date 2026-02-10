

def print_Message():
    print('hello')

def lambdamessage():print('hello')
lambdamessage()

def sume_(a,b):
    return a + b

print(sume_(2,13))

def lambda_(a,b): return a + b
print(lambda_(2,31))

print()

import random

num = [random.randint(-20,20) for i in range(10)]
def printlist(list_, promt=''):
    print(promt, end='\t')
    for item in list_:
        print(item, end='\t')
    print()

printlist(num, 'print list --> ')

def revMinus(n):
    if n > 0:
        return n * -1
    return n 

def revMinuslist(list_):
    clone = list_.copy()
    for i in range(len(clone)):
        clone[i] = revMinus(clone[i])
    return clone

print('='*50, '\n\n')
printlist(num, 'before list --> ')

clone =  revMinuslist(num)
printlist(clone, 'After list -->')
print('\n\n','='*50, '\n\n')


def test(n):
    return n**2

clone_2 = list(map(test,clone))
print(clone_2)
printlist(clone_2, 'After list -->')

clone_2 = list(map(lambda x: x*2,clone))
printlist(clone, 'After list -->')
printlist(clone_2, 'After list -->')

print('\n\n','='*50, '\n\n')

sales = [random.randint(100,1000) for i in range(10)]
printlist(sales, 'start sale --> ')
sales = map(lambda x: x - (x *.10), sales)
printlist(sales, 'end sale --> ')


# numb = input('enter numb --> ').split()
# numb = list(map(int , numb))
# print(sum(numb))

print('\n\n','='*50, '\n\n')

sales = [random.randint(-20,20) for i in range(10)]
printlist(sales, 'start --> ')
sales = list(filter(lambda x: x > 0 and x < 10, sales))
printlist(sales, 'end --> ')


print('\n\n','='*50, '\n\n')


# def spaw(a,b):
#     a,b = b,a

# a = 2
# b = 5

# revMinuslist(num)
# printlist(num)
    