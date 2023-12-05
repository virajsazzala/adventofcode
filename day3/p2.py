with open('data/inputs.txt', 'r') as f:
    d = f.readlines()

r = 0
for i in range(0, len(d), 3):
    c1, c2, c3 = map(str.strip, (d[i], d[i+1], d[i+2]))
    rt = list(set(c1) & set(c2) & set(c3))[0]
    r += ord(rt) - 96 if rt.islower() else ord(rt.lower()) - 96 + 26

print(r)