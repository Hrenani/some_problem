
def calculator():
    print('enter first number:')

    number1 = int(input())
    print('enter oprator to calculate:')

    oprator = input()

    print('enter seccond number')

    number2 = int(input())

    
    if oprator == '-':
        return f'your resulat is: {number1-number2}'
    elif oprator == '+':
        return  f"your result is:{number1+number2}"
    elif oprator == '*':
        return f'your result is: {number1*number2}'
    elif oprator == '/':
        return f'your result is: {number1/number2}'
    else:
        return 'invalid uprator. you must chose upragor between +,-,* or /'


while True:
    print(calculator())
