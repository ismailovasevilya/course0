n = int(input())
if n//100000 + n//10000%10 + n//1000%10 == n//100%10 + n//10%10 + n%10:
    print("Счастливый")
else:
    print("Обычный")