l=[2,8,5,4,16,25,9,15,2,15]
l2=[None]*len(l)
class process:
    def __init__(self,pid,size):
        self.size=size
        self.pid=pid
    def __str__(self):
        return f"Process ID: {self.pid}, Size: {self.size}\n"
def FirstFit(l:list,l2:list,l3:list):
    for i in range(len(l3)):
        flag=0
        for j in range(len(l)):
            if l[j]>=l3[i].size and l2[j] is None:
                l2[j]=f"P{l3[i].pid}:{l3[i].size}"
                flag=1
                break
        if flag==0:
            print(f"Process{i+1} cannot be accomodated.")


    print(" ","-"*80,sep="")
    print("|",end="")
    for i in l:
        print(i,end="\t|")
    print()
    print("|",end="")
    for i in l2:
        print(i,end="\t|")
    print()
    print(" ","-"*80,sep="")
processes=[process(1,4),
           process(2,16),
           process(3,15),
           process(4,20),
           process(5,15),
           process(6,9),
           process(7,1)]
print("First Fit Memory Allocation")
for i in processes:
    print(i)
FirstFit(l,l2,processes)

