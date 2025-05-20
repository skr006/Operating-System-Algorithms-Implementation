# Process Class
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


# Round Robin Scheduling Algorithm
def roundRobin(process_list: list, time_quantum: int):
    # Sort processes by arrival time
    process_list.sort(key=lambda p: p.ArrivalTime)
    ready_queue = [process_list[0]]
    total_burst = sum(p.BurstTime for p in process_list)
    timeline = [0]
    index = 1
    executed_order = []

    print("Ready Queue:")

    # First Phase: Main Round Robin loop
    for current_time in range(0, total_burst, time_quantum):
        current_proc = ready_queue.pop(0)
        current_proc.RemainingTime -= time_quantum
        executed_order.append(current_proc)

        # Enqueue new arrivals
        for i in range(index, len(process_list)):
            if process_list[i].ArrivalTime <= current_time + time_quantum:
                ready_queue.append(process_list[i])
                index += 1

        # Add back if not finished
        if current_proc.RemainingTime > 0:
            ready_queue.append(current_proc)
            timeline.append(timeline[-1] + time_quantum)
        else:
            # Adjust if over-executed
            if current_proc.RemainingTime == 0:
                timeline.append(timeline[-1] + time_quantum)
            else:
                timeline.append(timeline[-1] + time_quantum + current_proc.RemainingTime)

        # Print current ready queue
        for proc in ready_queue:
            print(f"Process {proc.pid}", end=" | ")
        print()

    # Second Phase: Finish remaining processes
    while ready_queue:
        current_proc = ready_queue.pop(0)
        current_proc.RemainingTime -= time_quantum
        executed_order.append(current_proc)

        if current_proc.RemainingTime > 0:
            ready_queue.append(current_proc)
            timeline.append(timeline[-1] + time_quantum)
        else:
            if current_proc.RemainingTime == 0:
                timeline.append(timeline[-1] + time_quantum)
            else:
                timeline.append(timeline[-1] + time_quantum + current_proc.RemainingTime)

    # Gantt Chart Output
    print("\nGantt Chart:")
    for proc in executed_order:
        print(f"Process {proc.pid}", end=" | ")
    print()

    # Calculate Completion, TAT, WT
    timeline.pop(0)
    executed_order.reverse()
    timeline.reverse()

    for proc in process_list:
        idx = executed_order.index(proc)
        proc.FinalTime = timeline[idx]
        proc.TurnAroundTime = proc.FinalTime - proc.ArrivalTime
        proc.WaitingTime = proc.TurnAroundTime - proc.BurstTime

    # Sort by PID for output
    process_list.sort(key=lambda p: p.pid)


# Driver Code
processes = [
    Process(1, 0, 5),
    Process(2, 1, 3),
    Process(3, 2, 1),
    Process(4, 3, 4),
    Process(5, 0, 2),
]

roundRobin(processes, time_quantum=2)
print("_" * 100)
for p in processes:
    print(p)
