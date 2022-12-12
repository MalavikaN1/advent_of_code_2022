f=open('./day10.txt',"r")
lines=f.readlines()


cycle=0
x=1
s=0
for line in lines:
    if line.startswith('noop'):
        cycle+=1
        if cycle in [20,60,100,140,180,220]:
            s+=x*cycle

    elif line.startswith('addx'):
        for i in range(2):
            cycle+=1
            if cycle in [20,60,100,140,180,220]:
                s+=x*cycle
    
        x+=int(line.strip().split(' ')[1])



print(s)