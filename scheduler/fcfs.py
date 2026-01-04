from .metrics import calculate_metrics

def fcfs(processes):
    time = 0
    processes.sort(key=lambda p: p.arrival)

    for p in processes:
        if time < p.arrival:
            time = p.arrival
        p.start_time = time
        time += p.burst
        p.completion_time = time

    return calculate_metrics(processes)
