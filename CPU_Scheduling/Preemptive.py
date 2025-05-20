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

def sort_procs(proc_list):
    return sorted(proc_list, key=lambda p: (p.arrv, p.pri))

def preemptive_sched(proc_list):
    curr_time = 0
    finished = 0
    gantt_chart = []

    while finished < len(proc_list):
        min_priority = float('inf')
        curr_proc = None

        for p in proc_list:
            if not p.completed and p.arrv <= curr_time and p.pri < min_priority:
                min_priority = p.pri
                curr_proc = p

        if curr_proc is None:
            curr_time += 1
            continue

        if curr_proc.start == -1:
            curr_proc.start = curr_time

        if not gantt_chart or gantt_chart[-1] != curr_proc.pid:
            gantt_chart.append(curr_proc.pid)

        curr_proc.remain -= 1

        if curr_proc.remain == 0:
            curr_proc.end = curr_time + 1
            curr_proc.completed = True
            finished += 1

        curr_time += 1

    return gantt_chart

def display_metrics(proc_list):
    print("| Process | Priority | Burst Time | Arrival Time | Start Time | End Time | Turnaround Time | Waiting Time |")
    print("|---------|----------|------------|--------------|------------|----------|------------------|--------------|")

    for p in proc_list:
        tat = p.end - p.arrv
        wt = tat - p.burst
        print(f"| {p.pid:>7} | {p.pri:>8} | {p.burst:>10} | {p.arrv:>12} | {p.start:>10} | {p.end:>8} | {tat:>16} | {wt:>12} |")

# Driver code
procs = [
    Proc(1, 3, 10, 0),
    Proc(2, 5, 5, 2),
    Proc(3, 1, 8, 1),
    Proc(4, 4, 3, 4),
    Proc(5, 2, 6, 3),
]

sorted_proc_list = sort_procs(procs)
gantt_output = preemptive_sched(sorted_proc_list)

print("Gantt Chart:")
print(" | ".join("Process " + str(pid) for pid in gantt_output))

display_metrics(sorted_proc_list)
