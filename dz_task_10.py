# task 1
# text = 'Ми зосереджені та енергійні перед матчем з! Леванте. Для нас це є ключова гра. Продовжити боротьбу за чемпіонство та зіграти на Сантьяго Бернабеу – це велика? мотивація. Хочемо провести чудовий матч. На базу зазвичай приходжу рано. Тут багато роботи, я говорив про це з першого дня.'
# count = 0
# for i in text:
#     if i == '.' or i == '!' or i == '?':
#         count+=1
# print('в тексті',count, 'речень')

# task 2

# polindrom = input('polindron : ')
# if polindrom == polindrom[::-1]:
#     print('слово', polindrom, 'є поліндром')
# elif polindrom == polindrom:
#     print('слово', polindrom,'не є поліндромом')


# task 3
# text = 'ми зосереджені ми енергійні це перед матчем з! Леванте. ми це є ключова гра.'
# reserved_words = ['ми']
# text1 = text.replace('ми', 'МИ')
# print(text1)


# print(text)



# task 4
# user = input('text -->')
# a = input('symvol_1 -->')
# b = input('symvol_2 -->')
# q = user.find(a)
# w = user.find(b)
# if q != -1 and q != -1:
#     user = user[:1] + user[w+1:]
# print(user)

# task 5

# text = input('text -->')            
# symbols = input('symvols -->')      
# words = text.split()            

# for w in words.copy():
#     for s in symbols:
#         if s in w:
#             words.remove(w)
#             break
#         # words1 = " ".join(words)

# print(words, end=" ")

# task 6

# text = input('text -->')
# word = text.split()
# text1 = " ".join(word[::-1])
# print(text1)


