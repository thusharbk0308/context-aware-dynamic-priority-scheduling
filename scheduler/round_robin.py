from collections import deque
from .metrics import calculate_metrics

def round_robin(processes, quantum=2):
    time = 0
    queue = deque()
    completed = []

    processes.sort(key=lambda p: p.arrival)

    while processes or queue:
        while processes and processes[0].arrival <= time:
            queue.append(processes.pop(0))

        if queue:
            p = queue.popleft()

            if p.start_time is None:
                p.start_time = time

            exec_time = min(quantum, p.remaining)
            time += exec_time
            p.remaining -= exec_time

            while processes and processes[0].arrival <= time:
                queue.append(processes.pop(0))

            if p.remaining > 0:
                queue.append(p)
            else:
                p.completion_time = time
                completed.append(p)
        else:
            time += 1

    return calculate_metrics(completed)
