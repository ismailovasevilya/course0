n = int(input())
if 0<=n<=1000:
    if n % 10 == 1 and n // 10 % 10 != 1:
        print(n, "программист")
    elif(n % 10 == 2 or n % 10 == 3 or n % 10 == 4) and (n // 10 % 10 != 1):
        print(n, "программиста")
    else:
        print(n, "программистов")