class Proc:
    def __init__(self, pid, pri, burst, arrv):
        self.pid = pid
        self.pri = pri
        self.burst = burst
        self.arrv = arrv
        self.remain = burst
        self.start = -1
        self.end = -1
        self.completed = False

def sort_procs(procs):
    return sorted(procs, key=lambda p: (p.arrv, p.pri))

def preemptive_sched(procs):
    time = 0
    completed = 0
    gantt = []

    while completed < len(procs):
        highest_pri = 1000000
        proc_to_run = None

        for proc in procs:
            if not proc.completed and proc.arrv <= time:
                if proc.pri < highest_pri:
                    highest_pri = proc.pri
                    proc_to_run = proc

        if proc_to_run is None:
            time += 1
            continue

        if proc_to_run.start == -1:
            proc_to_run.start = time
        if len(gantt)==0 or gantt[-1]!=proc_to_run.pid:
            gantt.append(proc_to_run.pid)
        proc_to_run.remain -= 1

        if proc_to_run.remain == 0:
            proc_to_run.end = time + 1
            proc_to_run.completed = True
            completed += 1

        time += 1

    return gantt

def display_metrics(procs):
    print("| Process | Priority | Burst Time | Arrival Time | Start Time | End Time | Turnaround Time | Waiting Time |")
    print("|---------|----------|------------|--------------|------------|----------|----------------|--------------|")

    for proc in procs:
        turnaround = proc.end - proc.arrv
        waiting = turnaround - proc.burst
        print(f"| {proc.pid:>7} | {proc.pri:>8} | {proc.burst:>10} | {proc.arrv:>12} | {proc.start:>10} | {proc.end:>8} | {turnaround:>14} | {waiting:>12} |")

procs = [
    Proc(1, 3, 10, 0),
    Proc(2, 5, 5, 2),
    Proc(3, 1, 8, 1),
    Proc(4, 4, 3, 4),
    Proc(5, 2, 6, 3),
]

sorted_procs = sort_procs(procs)

gantt = preemptive_sched(sorted_procs)

print("Gantt Chart:")
print(" | ".join("Process " + str(pid) for pid in gantt))

display_metrics(sorted_procs)
