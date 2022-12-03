f = open("./day_3_input", "r")
s=0
linearr=[]
arr=[]


# PART-1

# for lines in f:
#     first=lines[0:(len(lines))//2]
#     second = lines[len(lines)//2:]
#     for i in range(len(first)):
#         if(first[i] in second):
#             # if(first[i] not in arr):
#                 arr.append(first[i])
#                 break

# for i in range(len(arr)):
#     if(arr[i].islower()):
#         s+=((ord(arr[i]))-96)
#     if(arr[i].isupper()):
#         s+=(ord(arr[i]))-38

# print(s)


# --------------------------------------------------------------------------------------------------------------------------------

# PART-2

for lines in f:
    linearr.append(lines.strip())

for i in range(0,len(linearr),3):
    for x in linearr[i]:
        if x in linearr[i+1] and x in linearr[i+2]:
                arr.append(x)
                break

for i in range(len(arr)):
    if(arr[i].islower()):
        s+=((ord(arr[i]))-96)
    if(arr[i].isupper()):
        s+=(ord(arr[i]))-38

print(s)






        














