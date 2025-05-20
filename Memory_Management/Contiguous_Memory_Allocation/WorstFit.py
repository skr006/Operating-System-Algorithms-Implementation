MainMemory=[2,8,5,4,16,25,9,15,2,15]
AllocatedProcess=[None]*len(MainMemory)
class process:
    def __init__(self,pid,size) -> None:
        self.size=size
        self.pid=pid
    def __str__(self):
        return f"Process ID: {self.pid}, Size: {self.size}\n"
def WorstFit(l:list,m:list,p:list):
    for i in range(len(p)):
        f=0
        for j in range(len(l)):
            if l[j]>=l[f] and m[j] is None:
                f=j
        if l[f] >= p[i].size:
            m[f]=f"P{p[i].pid}:{p[i].size}"
        else:
            print(f"P{p[i].pid}:{p[i].size} Cannot be accomodated")

    print(" ","-"*80,sep="")
    print("|",end="")
    for i in l:
        print(i,end="\t|")
    print()
    print("|",end="")
    for i in m:
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
print("Worst Fit Memory Allocation")
for i in processes:
    print(i)
WorstFit(MainMemory,AllocatedProcess,processes)