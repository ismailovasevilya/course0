ans = 0
matches = 0
num = len(objects)
for i in range(len(objects)):
    for j in range(i + 1, len(objects)):
        if objects[i] == objects[j]:
            matches += 1
        if matches == 0:
            ans += 1
        matches = 0
print(ans)
