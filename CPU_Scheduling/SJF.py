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

def sjf(proc_list: list):
    proc_list.sort(key=lambda p: (p.ArrivalTime, p.BurstTime))
    ready_q = [proc_list[0]]
    total_bt = sum(p.BurstTime for p in proc_list)

    exec_time = 0
    next_idx = 1
    done = []

    while exec_time < total_bt:
        ready_q.sort(key=lambda p: p.BurstTime)
        curr = ready_q.pop(0)

        for i in range(next_idx, len(proc_list)):
            if proc_list[i].ArrivalTime <= exec_time + curr.BurstTime:
                ready_q.append(proc_list[i])
                next_idx += 1

        exec_time += curr.BurstTime
        done.append(curr)
        curr.FinalTime = exec_time
        curr.TurnAroundTime = curr.FinalTime - curr.ArrivalTime
        curr.WaitingTime = curr.TurnAroundTime - curr.BurstTime

    for p in done:
        print(f"Process {p.pid}", end=" | ")
    print()

# Driver code
processes = [
    Process(1, 0, 5),
    Process(2, 1, 3),
    Process(3, 2, 1),
    Process(4, 3, 4),
    Process(5, 4, 2),
]

sjf(processes)
print("_" * 100)
for p in processes:
    print(p)
