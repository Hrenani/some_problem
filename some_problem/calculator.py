###this problem is a simple calculator



def CalculateNumber():

    print('enter your first nubmer:')

    a = int(input())

    print('enter your uprator:')  #it can be / , * , + or -

    b = input()

    print('enter your seccond number:')

    c = int(input())

    try:
        if b == '/':
            print(f'your result is:{a/c}')
        elif b == '*':
            print(f'your result is: {a*c}')
        elif b == '+':
            print(f'your result is:{a+c}')
        else:
            print(f'your result is : {a-b}')
    except:
        print('uprator error.\n you must chose / , * , + or - uprator')

while True:
    CalculateNumber()

