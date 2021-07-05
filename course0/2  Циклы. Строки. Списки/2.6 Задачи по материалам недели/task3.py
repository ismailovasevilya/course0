lst = [int(i) for i in input().split()]
n = int(input())
m = []

for i in range(len(lst)):
    if lst[i] == n:
        print(i, end=' ')
if n not in lst:
    print("Отсутствует")
