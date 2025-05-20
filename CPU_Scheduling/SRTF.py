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

def srtf(proc_list: list):
    proc_list.sort(key=lambda p: p.ArrivalTime)
    ready_q = [proc_list[0]]
    total_time = sum(p.BurstTime for p in proc_list)

    next_idx = 1
    gant_seq = []
    timeline = [0]

    for curr_time in range(total_time):
        ready_q.sort(key=lambda p: p.RemainingTime)
        curr_proc = ready_q.pop(0)
        curr_proc.RemainingTime -= 1
        gant_seq.append(curr_proc)

        for i in range(next_idx, len(proc_list)):
            if proc_list[i].ArrivalTime <= curr_time + 1:
                ready_q.append(proc_list[i])
                next_idx += 1

        timeline.append(timeline[-1] + 1)
        if curr_proc.RemainingTime > 0:
            ready_q.append(curr_proc)

    # Process remaining (edge case)
    while ready_q:
        curr_proc = ready_q.pop(0)
        curr_proc.RemainingTime -= 1
        gant_seq.append(curr_proc)
        timeline.append(timeline[-1] + 1)
        if curr_proc.RemainingTime > 0:
            ready_q.append(curr_proc)

    print("\nGantt Chart:")
    i = 0
    while i < len(gant_seq) - 1:
        if gant_seq[i].pid == gant_seq[i + 1].pid:
            gant_seq.pop(i)
            timeline.pop(i + 1)
        else:
            i += 1
    for p in gant_seq:
        print(f"Process {p.pid}", end=" | ")
    print()

    # Final time, turnaround and waiting time calculation
    gant_seq.reverse()
    timeline.pop(0)
    timeline.reverse()
    for p in proc_list:
        idx = gant_seq.index(p)
        p.FinalTime = timeline[idx]
        p.TurnAroundTime = p.FinalTime - p.ArrivalTime
        p.WaitingTime = p.TurnAroundTime - p.BurstTime

    proc_list.sort(key=lambda p: p.pid)

# Driver code
processes = [
    Process(1, 0, 5),
    Process(2, 1, 3),
    Process(3, 2, 1),
    Process(4, 3, 4),
    Process(5, 4, 2),
]
srtf(processes)
print("_" * 100)
for p in processes:
    print(p)
