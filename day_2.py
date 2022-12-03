f = open("./day_2_input", "r")
a=[]
b=[]
s=0
# for lines in f:
#     if(lines[0]=='A'):
#         if(lines[2]=='X'):
#             s+=(1+3)
#         elif(lines[2]=='Y'):
#             s+=(2+6)
#         elif(lines[2]=='Z'):
#             s+=(3+0)
#     elif(lines[0]=='B'):
#         if(lines[2]=='X'):
#             s+=(1+0)
#         elif(lines[2]=='Y'):
#             s+=(2+3)
#         elif(lines[2]=='Z'):
#             s+=(3+6)
#     elif(lines[0]=='C'):
#         if(lines[2]=='X'):
#             s+=(1+6)
#         elif(lines[2]=='Y'):
#             s+=(2+0)
#         elif(lines[2]=='Z'):
#             s+=(3+3)

for lines in f:
    if(lines[0]=='A'):
        if(lines[2]=='X'):
            s+=(3+0)
        elif(lines[2]=='Y'):
            s+=(1+3)
        elif(lines[2]=='Z'):
            s+=(2+6)
    elif(lines[0]=='B'):
        if(lines[2]=='X'):
            s+=(1+0)
        elif(lines[2]=='Y'):
            s+=(2+3)
        elif(lines[2]=='Z'):
            s+=(3+6)
    elif(lines[0]=='C'):
        if(lines[2]=='X'):
            s+=(2+0)
        elif(lines[2]=='Y'):
            s+=(3+3)
        elif(lines[2]=='Z'):
            s+=(1+6)

print(s)