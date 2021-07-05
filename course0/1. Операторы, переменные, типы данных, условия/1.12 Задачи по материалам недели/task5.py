a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    if b <= c:
        print(a, '\n', b, '\n', c)
    else:
        print(a, '\n', c, '\n', b)

elif b >= a and b >= c:
    if a <= c:
        print(b, '\n', a, '\n', c)
    else:
        print(b, '\n', c, '\n', a)

elif c >= a and c >= b:
    if a <= b:
        print(c, '\n', a, '\n', b)
    else:
        print(c, '\n', b, '\n', a)