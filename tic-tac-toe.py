import random
bord = [[' ' for i in range(3)]for j in range(3)]
# print(bord)

def draw_bord(bord):
    print()
    for i in range(3):
        print(f'{bord[i][0]} {chr(9553)} {bord[i][1]} {chr(9553)} {bord[i][2]}')
        if i < 2:
            # print(chr(9580))
            print(chr(9552),chr(9580),chr(9552),chr(9580),chr(9552))
    print()
draw_bord(bord)



# def play(x):
#     for i in range(len(bord)):

    
