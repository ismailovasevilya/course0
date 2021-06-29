n1 = float(input())
n2 = float(input())
n3 = input()
if n3 == '+':
    print(n1+n2)
elif n3 == '-':
    print(n1-n2)
elif n3 == '/':
    if n2 == 0.0:
        print('Деление на 0!')
    else:
        print(n1/n2)
elif n3 == '*':
    print(n1*n2)
elif n3 == 'mod':
    if n2 == 0.0:
        print('Деление на 0!')
    else:
        print(n1 % n2)
elif n3 == 'pow':
    print(n1**n2)
elif n3 == 'div':
    if n2 == 0.0:
        print('Деление на 0!')
    else:
        print(n1//n2)