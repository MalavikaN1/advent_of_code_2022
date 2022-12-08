f=open('./day8inp',"r")
lines=f.readlines()
row=col=len(lines)
mat_row=mat_col=0

a = [ [0] * col for i in range(row) ]
for i in range(row):
    for j in range(col):
        a[i][j]=int(lines[i][j])


def part1():
    count=(row*2)+((col-2)*2)
    for i in range(1,row-1):
        for j in range(1,col-1):
            row_flag=True
            row2_flag=True
            col_flag=True
            col2_flag=True
            p=q=r=s=0
            b=a[i][j]
        
            for x in range(j):
                if a[i][x]>=b:
                    col_flag=False
                    break
            

            for y in range(j+1,col):
                    if a[i][y]>=b:
                        col2_flag=False
                        break

            for u in range(i):
                if a[u][j]>=b:
                    row_flag=False
                    break
            
            for v in range(i+1,row):
                if a[v][j]>=b:
                    row2_flag=False
                    break

            if row_flag is True or col_flag is True or row2_flag is True or col2_flag is True:
                count+=1

    print(count)


def part2():
    s=0
    for i in range(1,row-1):
        for j in range(1,col-1):
            left=right=top=bottom=0
            b=a[i][j]
        
            for x in range(j-1,-1,-1):
                if(b<=a[i][x]):
                    left+=1
                    break
                else:
                    left+=1


            for y in range(j+1,col):
                if(b<=a[i][y]):
                    right+=1
                    break
                else:
                    right+=1               

            for u in range(i-1,-1,-1):
                if(b<=a[u][j]):
                    top+=1
                    break
                else:
                    top+=1           
    
            
            for v in range(i+1,row):
                if(b<=a[v][j]):
                    bottom+=1
                    break
                else:
                    bottom+=1
            mul=left*right*top*bottom
            if(mul> s):
                s=mul
            left=right=top=bottom=0
    print(s)    


# part1()
part2()