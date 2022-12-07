f=open('./day7inp.txt','r')
lines=f.readlines()
tot=0
a={}
s=0

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child,size=0):
        self.child=child
        child.parent=self
        child.size=size
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            p=p.parent
            level+=1
        return level

    def print_tree(self):
        global a
        global s
        print('  '*self.get_level() + '|--', end = '')
        print(self.data)
        if self.children:
            for each in self.children:
                each.print_tree()


    def postOrder(self):
        global s
        if not self.children:
            return self.size
        tot=0
        for child in self.children:
            tot+=child.postOrder()
        a[self.data]=tot
        if(tot<100000):
                s+=tot
        return tot
        
            

            


root=TreeNode('/')
currentNode=root


for line in lines:
    if line.startswith("$ cd"):
        if ".." in line:
            currentNode=currentNode.parent
        else:
            dir_child=TreeNode(line.strip().split(' ')[2])
            currentNode.add_child(dir_child)
            currentNode=dir_child
    
    elif line.startswith("$ ls") or line.startswith("dir"):
        pass

    else:
        num=line.strip().split(' ')[0]
        currentNode.add_child(TreeNode( line.strip()),int(num))

root.postOrder()


print(s) #first part ans

maximum=max(a.values())
unused=70000000-maximum

del_num=[]

for i in sorted(a.values()):
    if unused+i>=30000000:
        del_num.append(i)


print(min(del_num))  #second part ans

