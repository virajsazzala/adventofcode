import re

with open("data/inputs.txt", "r") as f:
    d = f.readlines()

vs = [int("".join(re.findall(r"\d+", ln))) for ln in d]

rs = 0
for i in range(1, vs[0]):
    rm = (vs[0] - i) * i
    if rm > vs[1]: rs += 1

print(rs)
