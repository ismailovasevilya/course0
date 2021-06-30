a = [int(i) for i in input().split()]
for i in range(len(a)):
    if len(a) == 1:
        print(a[i], end='')
    elif i == 0:
        print(a[i+1] + a[len(a)-1], end=' ')
    elif i == (len(a)-1):
        print(a[0] + a[len(a)-2], end=' ')
    else:
        print(a[i-1] + a[i+1], end=' ')
