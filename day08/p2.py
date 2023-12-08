# NOTE: I didn't come up with the LCM method on my own. I took a hint from reddit

from math import gcd
import re

with open("/home/exvynai/code/dev/adventofcode/day08/data/inputs.txt", "r") as f:
    d = f.readlines()

ins = d[0].strip()


dt = {}
for ln in d[2:]:
    k, l, r = re.findall(r"[A-Z]+", ln)
    dt[k] = [l, r]

sts = [key for key in dt if key.endswith("A")]

cys = []
for st in sts:
    cy = []

    cs = ins
    stc = 0
    iz = None

    while True:
        while stc == 0 or not st.endswith("Z"):
            stc += 1
            if cs[0] == "L":
                st = dt[st][0]
            else:
                st = dt[st][1]
            cs = cs[1:] + cs[0]

        cy.append(stc)

        if iz is None:
            iz = st
            stc = 0
        elif st == iz:
            break

    cys.append(cy)

vs = [cy[0] for cy in cys]

lcm = vs[0]

for v in vs:
    lcm *= v // gcd(lcm, v)

print(lcm)
