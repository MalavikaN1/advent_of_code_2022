f = open("./input.txt", "r")
s=0
arr=[]
for line in f:
    if(line!='\n'):
        s+=int(line)
    else:
        arr.append(s)
        s=0

print(max(arr))

arr.sort(reverse=True)
print(arr[0]+arr[1]+arr[3])