s = str(input())
t = str(input())
count = 0
n = len(s)
for i in range(n):
    newstring = s[i:n]
    t = t.lower()
    if newstring.lower().startswith(t) == True:
        count += 1
print(count)

