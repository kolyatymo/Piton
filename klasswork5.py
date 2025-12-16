
# day = int(input("days : "))



# if day == 3:
#     print('monday')
# elif day == 2:
#     print('tuesday')
# elif day == 1:
#     print('Wednesday')
# elif day == 1:
#     print('Wednesday')   
# elif day == 1:
#     print('Wednesday')
# elif day == 1:
#     print('Wednesday')
# elif day == 1:
#     print('Wednesday')         
# else:
#     print('error')

# match day:
#     case 1:
#         print('monday')
#     case 2:
#         print('tuesday')
#     case 3:
#         print('3')
#     case 4:
#         print('4')
#     case 5:
#         print('5')
#     case 6:
#         print('tuesday')    
#     case _:
#         print('error')      
# 
# '''
# 31.03.2025 --> 01.04.2025
# 28.02.2004 --> 29.02.2004
# 28.02.2005 --> 01.03.2005
# 31.12.2025 --> 01.01.2026
# '''

# day = int(input("days : "))
# month = int(input("month : "))
# years = int(input("year : "))

# day_of_month = 0

# print(f"{"0" if day < 10 else ""}{day}.{"0" if month < 10 else ""}{month}.{years}")
# match month:
#     case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#       day_of_month = 31
#     case 2:
#     #   if years % 4 == 0 and years % 100 != 0 or years % 400 ==0:
#     #      day_of_month = 29
#     #   else:
#     #      day_of_month = 28
#      day_of_month = 29 if years % 4 == 0 and years % 100 != 0 or years % 400 == 0 else 28
#     case 4 | 6 | 9 | 11:
#       day_of_month = 30


# day+=1
# if day > day_of_month:
#     day = 1
#     month +=1
# if month > 12:
#     month = 1
#     years += 1  

# print(f"{"0" if day < 10 else ""}{day}.{"0" if month < 10 else ""}{month}.{years}")

# print(f"days : {day_of_month}")      

    #   day_of_month = 30
    # case 5:
    #   day_of_month = 31
    # case 6:
    #   day_of_month = 30
    # case 7:
    #   day_of_month = 31
    # case 8:
    #   day_of_month = 31
    # case 9:
    #   day_of_month = 30
    # case 10:
    #   day_of_month = 31
    # case 11:
    #   day_of_month = 30
    # case 12:
    #   day_of_month = 31


# task 1
# seconds = int(input("seconds : "))
# second_mins_hours = input("second or mins or hours : ")
# if second_mins_hours == "second":
#    second = 86400 - seconds
#    print("secon : ", second)
# elif second_mins_hours == "hours":
#    hour = seconds // 3600
#    hour1 = 24 - hour
#    print("hours : ", hour1)
# elif second_mins_hours == "mins":
#    min = seconds // 60
#    mi1 = 1440 - min
#    print("mins : ", mi1)

# task 2
# diameter = int(input("diameter : "))
# p_R = input("P? or S? : ")
# if p_R == "P":
#    per = 3.14 * diameter 
#    print("P = ",per)
# if p_R == 'S':
#    r = diameter / 2
#    s = 3.14 * (diameter * 2) / 4
#    print("S = ",s) 

# task 3
# sume = int(input("sume : "))
# number = int(input("number : "))
# interest = int(input("interest : "))
# sum_num_int = input("sume all or sume one : ")
# if sum_num_int == "sume all":
#     sumee = sume * number
#     print('sume all : ', sumee)
# if sum_num_int == "sume one":
#     sume1 = sume * (1 - interest / 100)   
#     print(sume1) 

# task 4
# rozmai_GB = int(input("File GB : "))
# wife_speed = int(input("wife bit : "))
# hours_mins_second = input("hours or mins or second : ")
# if hours_mins_second == "hours":
#     gb_bit = rozmai_GB * 8000000000
#     hour = 3600 * (gb_bit // wife_speed)
#     print(hour)
# elif hours_mins_second == "mins":
#     min_bit = rozmai_GB * 8000000000
#     min = 60 * (gb_bit // wife_speed)
#     print(min)
# elif hours_mins_second == "second":
#     print(8000000000 / rozmai_GB)    


# task 5
# hours = int(input("hours : "))
# if hours >= 0 and hours <= 6:
#     print("Good night")
# elif hours >= 6 and hours <= 13:
#     print("Good Morning")
# elif hours >= 13 and hours <= 17:
#     print("Good Day")
# elif hours >= 17 and hours <= 24:
#     print("Good Evening")           

# task 6
# tem = int(input("temperature : "))
# if tem < -10:
#     print('Дуже холодно')
# elif tem >= -10 and tem < 0:
#     print("Холодно")    
# elif tem >= 0 and tem < 15:
#     print("Прохолодно")    
# elif tem >= 15 and tem < 25:
#     print("Тепло")    
# elif tem >= 25:
#     print("Спекотно")                