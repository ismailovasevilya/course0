n =  int(input())
known = []
for i in range(n):
    x = input().lower()
    if x not in known:
        known.append(x)

checked = []
l = int(input)
for j in range(l):
    x = input().lower().split()
    for i in x:
        if i not in known and i not in checked:
            checked.append(i)

print('\n'.join(checked))