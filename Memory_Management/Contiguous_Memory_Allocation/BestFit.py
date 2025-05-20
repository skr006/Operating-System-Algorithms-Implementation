l=[2,8,5,4,16,25,9,15,2,15]
l2=[None]*len(l)
class process:
    def __init__(self,pid,size) -> None:
        self.size=size
        self.pid=pid
    def __str__(self):
        return f"Process ID: {self.pid}, Size: {self.size}\n"
def BestFit(MainMemory:list,AllocatedProcess:list,processes:list):
    for i in range(len(processes)):
        x=processes[i].size
        m=[]
        for j in range(len(MainMemory)):
            if AllocatedProcess[j] is None and x<=MainMemory[j]:
                m.append((MainMemory[j],j))
        if m!=[]:
            m.sort(key=lambda x:x[0])
            AllocatedProcess[m[0][1]]=f"P{processes[i].pid}:{processes[i].size}"
        else:
            print(f"Process{i+1} cannot be accomodated.")
    print(" ","-"*80,sep="")
    print("|",end="")
    for i in MainMemory:
        print(i,end="\t|")
    print()
    print("|",end="")
    for i in AllocatedProcess:
        print(i,end="\t|")
    print()
    print(" ","-"*80,sep="")


# Driver code
processes=[process(1,4),
           process(2,16),
           process(3,15),
           process(4,20),
           process(5,15),
           process(6,9),
           process(7,1)]
print("Best Fit Memory Allocation")
for i in processes:
    print(i)
BestFit(l,l2,processes)

