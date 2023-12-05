with open('data/inputs.txt', 'r') as f:
    d = map(str.strip, f.readlines())

r = 0
for ln in d:
    e1, e2 = ln.split(',')
    e1 = list(map(int, e1.split('-')))
    e2 = list(map(int, e2.split('-')))
    
    if (
        e1[0] <= e2[0] 
        and e1[1] >= e2[1]
        or e2[0] <= e1[0] 
        and e2[1] >= e1[1]
    ):
        print('yes')
        r += 1

print(r)