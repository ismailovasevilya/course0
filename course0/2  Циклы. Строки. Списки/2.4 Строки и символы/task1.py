s = input()
num = s.count('c') + s.count('C') + s.count('g') + s.count('G')
print(num/len(s) * 100)
