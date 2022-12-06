from collections import Counter
f = open("./day6inp", "r")
i=0
lines=f.readlines()
def part1():
    for line in lines:
        while((i+4)<len(line)):
            strng=line[i:i+4]
            a=Counter(strng)
            if len(a)==4:
                xyz=i+4
                break
            i+=1
    print(xyz)

def part2():
    for line in lines:
        while((i+4)<len(line)):
            strng=line[i:i+14]
            a=Counter(strng)
            if len(a)==14:
                xyz=i+14
                break
            i+=1
    print(xyz)  


# part1()
# part2()