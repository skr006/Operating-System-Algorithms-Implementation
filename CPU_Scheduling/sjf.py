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
    
def sjf(lst:list):
    lst.sort(key=lambda x:(x.ArrivalTime,x.BurstTime))
    q=[lst[0]]
    s=0
    for i in lst:
        s+=i.BurstTime
    j=1
    i=0
    l=[]
    t=[]
    while i<s:
        q.sort(key=lambda x:x.BurstTime)
        x=q.pop(0)
        for h in range(j,len(lst)):
            if lst[h].ArrivalTime<=x.BurstTime+i:
                q.append(lst[h])
                j+=1
        
        i=x.BurstTime+i
        l.append(x)
        x.FinalTime=i
        x.TurnAroundTime=x.FinalTime-x.ArrivalTime
        x.WaitingTime=x.TurnAroundTime-x.BurstTime
    for i in l:
        print(f"Process {i.pid}",end=" | ")
    print()
processes = [
        Process(1, 0, 5),
        Process(2, 1, 3),
        Process(3, 2, 1),
        Process(4, 3, 4),
        Process(5, 4, 2),
    ]
sjf(processes)
print("_"*100)
for i in processes:
    print(i)
