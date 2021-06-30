s = str(input())
i = len(s) - 1
print(i)
count = 1
k = 0
t = ''
if len(s) == 1:
    t = t + s + str(count)
else:
    for j in range(i):

        if s[k] == s[j + 1]:
            count += 1
        elif s[k] != s[j + 1]:
            t = t + s[k] + str(count)
            k = j + 1
            count = 1
    for j in range(i, i + 1):
        if s[-1] == s[-2]:
            t = t + s[j] + str(count)
        elif s[-1] != s[-2]:
            t = t + s[j] + str(count)
            count = 1
print(t)







