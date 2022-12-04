f = open("./day4inp", "r")
cnt=0
for lines in f:
    x=lines.strip().split(',')
    a,b=x[0].split('-')
    c,d=x[1].split('-')
    if set((range(int(a),int(b)+1))).issubset(range(int(c),int(d)+1)) or set((range(int(c),int(d)+1))).issubset(range(int(a),int(b)+1)) or set((range(int(a),int(b)+1))).intersection(set((range(int(c),int(d)+1)))) :
        cnt=cnt+1
print (cnt)
