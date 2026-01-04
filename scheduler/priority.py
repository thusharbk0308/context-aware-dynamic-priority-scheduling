from .metrics import calculate_metrics

def priority_scheduling(processes):
    time = 0
    completed = []
    ready = []

    processes.sort(key=lambda p: p.arrival)

    while processes or ready:
        while processes and processes[0].arrival <= time:
            ready.append(processes.pop(0))

        if ready:
            ready.sort(key=lambda p: p.priority, reverse=True)
            p = ready.pop(0)
            p.start_time = time
            time += p.burst
            p.completion_time = time
            completed.append(p)
        else:
            time += 1

    return calculate_metrics(completed)
