import re

with open("data/inputs.txt", "r") as f:
    d = f.readlines()

vs = [list(map(int, re.findall(r"\d+", ln))) for ln in d]

rs = 1
for i, v in enumerate(vs[0]):
    rt = 0
    for j in range(1, v):
        rm = (v - j) * j
        if rm > vs[1][i]: rt += 1

    rs *= rt

print(rs)
