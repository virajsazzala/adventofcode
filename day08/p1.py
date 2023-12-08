import re

with open("/home/exvynai/code/dev/adventofcode/day08/data/inputs.txt", "r") as f:
    d = f.readlines()

ins = d[0].strip()
ins *= 100


dt = {}
for ln in d[2:]:
    k, l, r = re.findall(r"[A-Z]+", ln)
    dt[k] = [l, r]

st = "AAA"

for i, v in enumerate(ins):
    if st == "ZZZ":
        print(i)
        break
    if v == "L":
        st = dt[st][0]
    else:
        st = dt[st][1]
