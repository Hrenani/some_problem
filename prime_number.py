#this problem declar prime number that there are between to number which you say

import math

def Prime_number():
    print('enter two positive number to find Prime number between theme')
    number1 = int(input())
    number2 = int(input())

    List_pirmeNumber = []

    for i in range(number1,number2+1):
        a = True
        I = int(math.sqrt(i))
        for j in range(2,i):
            if i%j == 0:
                a = False
        if a == True and i !=1:
            List_pirmeNumber.append(i)

    return List_pirmeNumber

print(Prime_number())
