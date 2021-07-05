s1 = input()
s2 = input()
s3 = input()
s4 = input()

encode = {}
decode = {}

for i in range(len(s1)):
    encode.update([(s1[i], s2[i])])
    decode.update([(s2[i], s1[i])])

res1 = []
for sign in encode:
    res1.append(s3[sign])

res2 = []
for sign in decode:
    res2.append(s4[sign])




