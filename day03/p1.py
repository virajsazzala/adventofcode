with open('data/inputs.txt', 'r') as f:
    d = f.readlines()

r = 0
for ln in d:
    mid = len(ln) // 2
    c1, c2 = ln[:mid], ln[mid:]
    rt = list(set(c1) & set(c2))[0]
    r += ord(rt) - 96 if rt.islower() else ord(rt.lower()) - 96 + 26

print(r)