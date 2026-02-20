import json

library = 'data.json'
directory = 'file_practic'
FILE_ = f'{directory}/{library}'


def loadFile():
    try:
        with open(FILE_, encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError as ex:
        print('file not found',ex)
        return[]


file_ = loadFile()


def save():
    with open(FILE_, 'w', encoding='utf-8') as file:
        json.dump(file_, file, ensure_ascii=False, indent=4)




def review():
    if not file_:
        print('library empty')
        return

    for i in file_:
        print(i)

def add():
    type_ = input('книга - журнал - газета --> ').strip().lower()
    if type_ not in ('книга', 'журнал','газета'):
        print('invalid type')
        return


    title = input('name --> ')
    author = None
    category = None
    year = None

    if type_ == 'книга':
        author = input('author --> ')
        category = input('category --> ')
        year = int(input('year --> '))
    else:
        year = int(input('year --> '))

    shelf = {
        'type': type_,
        'title': title,
        'author': author,
        'category': category,
        'year': year,
        'available': True
    }

    file_.append(shelf)
    save()
    print('append')
def addition():
    n = int(input('how much add --> '))
    for _ in range(n):
        add()


def remove():
    type_ = input('книга - журнал - газета --> ').strip().lower()
    title = input('name for delete --> ').strip()
    year = int(input('year for delete --> '))
    for index, i in enumerate(file_):
        if i['title'] == title and i['year'] == year and i['type'] == type_:
            del file_[index]
            save()
            print('delete')
            return
    print('not found')



def arrange():
    file_.sort(key=lambda x: (x['type'], x['title']))
    save()
    print('sorted')


def search():
    author = input('author --> ')
    title = input('name --> ')

    for i in file_:
        if i['type'] == 'книга' and i['author'] == author and i['title'] == title:
            if i['available']:
                print('is in stock')
            else:
                print('issued')
            return

    print('not found')

def searchM():
    name = input('name magazine --> ')
    for i in file_:
        if i['type'] == 'журнал' and i['title'] == name:
            if i['available']:
                print('is in stock')
            else:
                print('issued')
            return

    print('not found')

def findA():
    autor = input('author --> ')
    for i in file_:
        if i['type'] == 'книга' and i['author'] == autor:
            print(i)

def category_():
    category = input('category --> ')
    for i in file_:
        if i['type'] == 'книга' and i['category'] == category:
            print(i)

def magazineY():
    name = input('name --> ')
    year = int(input('year --> '))
    for i in file_:
        if i['type'] == 'журнал' and i['title'] == name and i['year'] == year:
            print(i)

def countbook():
    category = input('category --> ')
    count_ = 0
    for i in file_:
        if i['type'] == 'книга' and i['category'] == category:
            count_ +=1
        
    print(f'{count_} категорії {category}')

def removeM():
    global file_
    year = int(input('year for delete --> '))
    file_ = [i for i in file_ if not (i['type'] == 'газета' and i['year'] == year)]
    save()
    print('delete')

def debtors():
    autor = input('author --> ')
    found = False
    for i in file_:
        if i['type'] == 'книга' and i['author'] == autor and i['available'] == False:
            print(i)
            found = True

    if not found:
        print('there are no deptors')


while True:
        print('''
1 - review
2 - add
3 - delete 
4 - sort
5 - found book
6 - found magazine
7 - found book for author
8 - found book for category
9 - found magazine for title and year
10 - books count by category
11 - delete newspapers by year
12 - deptor of books
13 - Add multiple records
0 - exit
''')

        choice = input('choose --> ')

        if choice == '1':
            review()
        elif choice == '2':
            add()
        elif choice == '3':
            remove()
        elif choice == '4':
            arrange()
        elif choice == '5':
            search()
        elif choice == '6':
            searchM()
        elif choice == '7':
            findA()
        elif choice == '8':
            category_()
        elif choice == '9':
            magazineY()
        elif choice == '10':
            countbook()
        elif choice == '11':
            removeM()
        elif choice == '12':
            debtors()
        elif choice == '13':
            addition()
        elif choice == '0':
            break
        else:
            print('selected')