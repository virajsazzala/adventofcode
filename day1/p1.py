with open('data/inputs.txt', 'r') as f:
    d = f.readlines()

rs = []
tmp = 0
for ln in d:
   if ln == '\n':
        rs.append(tmp)
        tmp = 0
        continue
   tmp += int(ln.strip())
       
print(max(rs))