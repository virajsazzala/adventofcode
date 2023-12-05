def outcome(p1, p2):
    ss = {"X": 1, "Y": 2, "Z": 3}    

    # loss
    tmp = ''
    if p2 == 'X':
        if p1 == 'A': tmp = 'Z'
        elif p1 == 'B': tmp = 'X'
        else: tmp = 'Y'
        return ss[tmp]

    # draw
    if p2 == 'Y':
        if p1 == 'A': tmp = 'X'
        elif p1 == 'B': tmp = 'Y'
        else: tmp = 'Z'
        return ss[tmp] + 3
    
    # win
    if p2 == 'Z':
        if p1 == 'A': tmp = 'Y'
        elif p1 == 'B': tmp = 'Z'
        else: tmp = 'X'
        return ss[tmp] + 6

with open("data/inputs.txt", "r") as f:
    d = f.readlines()

r = 0
for ln in d:
    p1, p2 = ln.strip().split(" ")
    r += outcome(p1, p2)

print(r)
