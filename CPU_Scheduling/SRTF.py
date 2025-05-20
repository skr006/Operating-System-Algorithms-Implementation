class Process:
    def __init__(self, pid: int, at: int, bt: int) -> None:
        self.pid = pid
        self.ArrivalTime = at
        self.BurstTime = bt
        self.RemainingTime = bt
        self.FinalTime = 0
        self.TurnAroundTime = 0
        self.WaitingTime = 0
    def __str__(self) -> str:
        return f"Process {self.pid}: FinalTime={self.FinalTime}, TurnAroundTime={self.TurnAroundTime}, WaitingTime={self.WaitingTime}"

def srtf(lst:list):
    lst.sort(key=lambda x:x.ArrivalTime)
    q=[lst[0]]
    s=0
    for i in lst:
        s+=i.BurstTime
    j=1
    l=[]
    t=[]
    t.append(0)
    for i in range(s):
        q.sort(key=lambda x:x.RemainingTime)
        x=q.pop(0)
        x.RemainingTime-=1
        l.append(x)
        for h in range(j,len(lst)):
            if lst[h].ArrivalTime<=i+1:
                q.append(lst[h])
                j+=1
        if x.RemainingTime>0:
            q.append(x)
            t.append(t[len(l)-1]+1)
        elif x.RemainingTime<=0:
            t.append(t[len(l)-1]+1)
    while q!=[]:
        x=q.pop(0)
        x.RemainingTime=x.RemainingTime-1
        l.append(x)
        if x.RemainingTime>0:
            q.append(x)
            t.append(t[len(l)-1]+1)
        elif x.RemainingTime<=0:
            t.append(t[len(l)-1]+1)
    print("\nGant Chart:")
    i=0
    while True:
        n=len(l)
        if i==n-1:
            break
        if l[i].pid == l[i+1].pid:
            l.pop(i)
        else:
            i+=1
    for i in l:
        print(f"Process {i.pid}",end=" | ")
    print()
    t.pop(0)
    x=0
    l=l[::-1]
    t=t[::-1]
    for i in lst:
        lst[lst.index(i)].FinalTime=t[l.index(i)]
        lst[lst.index(i)].TurnAroundTime=lst[lst.index(i)].FinalTime-lst[lst.index(i)].ArrivalTime
        lst[lst.index(i)].WaitingTime=lst[lst.index(i)].TurnAroundTime-lst[lst.index(i)].BurstTime

    lst.sort(key=lambda x:x.pid)
processes = [
        Process(1, 0, 5),
        Process(2, 1, 3),
        Process(3, 2, 1),
        Process(4, 3, 4),
        Process(5, 4, 2),
    ]
srtf(processes)
print("_"*100)
for i in processes:
    print(i)