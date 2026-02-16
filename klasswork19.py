import json


# student = {
#     'name':'Nazar',
#     'lastname':'Bondar',
#     'age':15
# }

directory = '19.files'
file_out = 'data.txt'

# json_serial = json.dumps(student)
# print(json_serial, type(json_serial))

# # with open(f'{directory}/{file_out}','w') as file:
# #     file.write(json_serial)

# with open(f'{directory}/{file_out}') as file:
#     result = file.read()

# result = json.loads(result)
# print(result['age'], type(result))

# group = [
#   {
#     "first_name": "Nicola",
#     "last_name": "Hammatt",
#     "email": "nhammatt0@businesswire.com"
#   },
#   {
#     "first_name": "Claus",
#     "last_name": "Chamberlayne",
#     "email": "cchamberlayne1@squidoo.com"
#   },
#   {
#     "first_name": "Ofelia",
#     "last_name": "Sherston",
#     "email": "osherston2@mlb.com"
#   },
#   {
#     "first_name": "Robby",
#     "last_name": "Hallock",
#     "email": "rhallock3@diigo.com"
#   },
#   {
#     "first_name": "Louise",
#     "last_name": "Sugg",
#     "email": "lsugg4@toplist.cz"
#   },
#   {
#     "first_name": "Annamaria",
#     "last_name": "Mohring",
#     "email": "amohring5@microsoft.com"
#   },
#   {
#     "first_name": "Shanan",
#     "last_name": "Fergie",
#     "email": "sfergie6@dagondesign.com"
#   },
#   {
#     "first_name": "May",
#     "last_name": "Knaggs",
#     "email": "mknaggs7@un.org"
#   },
#   {
#     "first_name": "Xena",
#     "last_name": "Ramberg",
#     "email": "xramberg8@seesaa.net"
#   },
#   {
#     "first_name": "Jamison",
#     "last_name": "Yeeles",
#     "email": "jyeeles9@devhub.com"
#   }
# ]

# # group.sort(key= lambda x: x['last_name'])

# group = list(filter(lambda x: len(x['first_name']) > 4,group))

# with open(f'{directory}/{file_out}', 'w') as file:
#     # file.write(json.dumps(group))
#     json.dump(group,file)




# with open(f'{directory}/{file_out}') as file:
#     # resul = json.loads(file.read())
#     resul = json.load(file)

# print(resul, type(resul))

# for item in resul:
#     print(item)
#     for key, value in item.items():
#         item[key] = value.upper()

# print()
# for item in resul:
#     print(item)

import json
import requests

# url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

# result = requests.get(url).json()
# print(result)

url = 'https://pixabay.com/api/?key=14304821-db198647e0592cf253911c94a&q=yellow+flowers&image_type=photo'
res = requests.get(url).json()
image = res['hits']
print(image)

coun = 1

for img in image:
    with open(f'{directory}/img/{coun}.jpg', 'wb') as file:
        file.write(requests.get(img['webformatURL']).content)
    coun += 1