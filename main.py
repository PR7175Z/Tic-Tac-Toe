import os
import msvcrt
import time

winner = False

def winnerval():
    print(f'{ch} wins')
    exit()

x = 0
ch = 0
arr = [[0 for i in range(0, 3)] for j in range(0,3)]
while x < 10:
    os.system('cls')
    for m in range(0, 3):
        for o in range(0,3):
            print(arr[m][o], end='\t' )
        print("\n")

    col = 0
    row = 0
    if(x%2 == 0):
        ch = 'X'
    else:
        ch = 'O'

    num = int(input("Enter a number"))
    if(num >= 4):
        row = num - 4
        col = col+1
        if(row > 2):
            row = row - 3
            col = col+1
        x = x+1
    elif(num == 0):
        print("invalid input")
        if(x != 0):
            x = x
        else:
            x = 0
        ch = 0
    else:
        row = num -1
        x = x+1
        
    if(arr[col][row] != 0):
        print('error')
        x = x-1
    else:
        arr[col][row] = ch
    
    for h in range(0, 3):
        if(arr[h][0]==arr[h][1]==arr[h][2]=='X' or arr[h][0]==arr[h][1]==arr[h][2]=='O'):
            winnerval()
            break
        elif(arr[0][h]==arr[1][h]==arr[2][h]=='X' or arr[0][h]==arr[1][h]==arr[2][h]=='O'):
            winnerval()
            break
        elif(arr[0][0]==arr[1][1]==arr[2][2]=='X' or arr[0][0]==arr[1][1]==arr[2][2]=='O'):
            winnerval()
            break
        elif(arr[0][2]==arr[1][1]==arr[2][0]=='X' or arr[0][2]==arr[1][1]==arr[2][0]=='O'):
            winnerval()
            break
        else:
            continue
