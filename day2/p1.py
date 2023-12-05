def outcome(p1, p2):
    ss = {"X": 1, "Y": 2, "Z": 3}

    # draw
    if (
        p1 == "A" and p2 == "X"
        or p1 == "B" and p2 == "Y"
        or p1 == "C" and p2 == "Z"
    ):
        return ss[p2] + 3

    # loss
    if (
        p1 == "A" and p2 == "Z" 
        or p1 == "B" and p2 == "X" 
        or p1 == "C" and p2 == "Y"
    ):
        return ss[p2]

    # win
    if (
        p1 == "A" and p2 == "Y" 
        or p1 == "B" and p2 == "Z" 
        or p1 == "C" and p2 == "X"
    ):
        return ss[p2] + 6
    

with open("data/inputs.txt", "r") as f:
    d = f.readlines()

r = 0
for ln in d:
    p1, p2 = ln.strip().split(" ")
    r += outcome(p1, p2)

print(r)
