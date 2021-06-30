a = int(input())
b = int(input())
s = 0;
j = 0;
if a % 3 == 0:
    for i in range(a, b + 1, 3):
        s += i
        j += 1
elif a % 3 != 0:
    a += 1
    if a % 3 == 0:
        for i in range(a, b + 1, 3):
            s += i
            j += 1
    else:
        a += 1
        if a % 3 == 0:
            for i in range(a, b + 1, 3):
                s += i
                j += 1
print(s / j)
