from .metrics import calculate_metrics

def dynamic_priority(p, current_time):
    waiting = current_time - p.arrival
    waiting_score = min(waiting, 5)

    short_burst_score = 1 / p.remaining
    burst_score = min(short_burst_score * 4, 2)

    io_boost = 3 if p.io_bound else 0
    fg_boost = 3 if p.foreground else 0

    energy_penalty = 0.2 * p.burst

    return (
        p.priority * 2 +
        waiting_score +
        burst_score +
        io_boost +
        fg_boost -
        energy_penalty
    )


def cadps(processes):
    time = 0
    completed = []
    ready = []
    timeline = []

    processes.sort(key=lambda p: p.arrival)

    while processes or ready:
        while processes and processes[0].arrival <= time:
            ready.append(processes.pop(0))

        if ready:
            ready.sort(
                key=lambda p: dynamic_priority(p, time),
                reverse=True
            )

            p = ready[0]

            if p.start_time is None:
                p.start_time = time
                p.response_time = time - p.arrival

            timeline.append(f"P{p.pid}")
            p.remaining -= 1
            time += 1

            while processes and processes[0].arrival <= time:
                ready.append(processes.pop(0))

            if p.remaining == 0:
                p.completion_time = time
                completed.append(p)
                ready.remove(p)
        else:
            timeline.append("IDLE")
            time += 1

    result = calculate_metrics(completed)
    result["timeline"] = timeline
    return result
