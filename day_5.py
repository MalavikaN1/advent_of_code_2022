

f = open("./day5_inp.txt", "r")
a=[]
arr={1:['F','C','P','G','Q','R'],
      2:['W','T','C','P'],
      3:['B','H','P','M','C'],
      4:['L','T','Q','S','M','P','R'],
      5:['P','H','J','Z','V','G','N'],
      6:['D','P','J'],
      7:['L','G','P','Z','F','J','T','R'],
      8:['N','L','H','C','F','P','T','J'],
      9:['G','V','Z','Q','H','T','C','W']
    }

lines=f.readlines()

def part1():
    for line in lines:
        res = [int(i) for i in line.split() if i.isdigit()]
        for j in range(0,res[0]):
            a=arr[res[1]].pop()
            arr[res[2]].append(a)
        

    print(arr)

# part1()



def part2():
    for line in lines:
        a=[]
        res = [int(i) for i in line.split() if i.isdigit()]
        for j in range(0,res[0]):
            a.append(arr[res[1]].pop())
        arr[res[2]]=arr[res[2]]+a[::-1]

    print(arr)

# part2()















