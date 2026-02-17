# try:
#     number = int(input('enter --> '))
#     print(f'Res {number}')
#     print('finely program')
# except ValueError:
#     print('error number')
# else:
#     print('run block else')
# finally:
#     print('finaly')

# print('end')

# try:
#     number_1 = int(input('numb 1 -->'))
#     number_2 = int(input('numb 2 -->'))
#     print(f'res {number_1}/{number_2} = {number_1/number_2}')
# except ValueError as ex:
#     print('value error',ex)
# except ZeroDivisionError as ex:
#     print('value error',ex)
# except Exception as ex:
#     print('value error',ex)

# print('finally program')

# while True:
#     try:
#         number_1 = int(input('numb 1 -->'))
#         number_2 = int(input('numb 2 -->'))
#         print(f'res {number_1}/{number_2} = {number_1/number_2}')
#         break
#     except (ValueError,ZeroDivisionError) as ex:
#         print('value error or zeroerror',ex)
#     except Exception as ex:
#         print('value error',ex)

# print('finally program')


def prinNumb(numb):
    if numb < 0:
        raise ValueError('number < 0')
    if numb > 10000:
        raise OverflowError('number > 10000')
    print(f'ok --> {numb}')

try:

    prinNumb(7)
except Exception as ex:
    print('error',ex)
print('finnaly program')

def division(a,b):
    try:
        print(f'{a} / {b} = {a / b}')
    except Exception as ex:
        print('zerroerror',ex)


division('4',0)

print('finnaly program')


