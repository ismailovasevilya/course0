b = True
while b:
    n = int(input())
    if n < 10:
        continue
    elif n > 100:
        b = False
        break
    else:
        print(n)
