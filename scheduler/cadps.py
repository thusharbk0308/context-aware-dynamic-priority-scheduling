from .metrics import calculate_metrics

def estimate_cpu_usage(burst):
    if burst > 15:
        return "High"
    elif burst >= 7:
        return "Medium"
    else:
        return "Low"

def estimate_energy(burst):
    return round(burst * 0.2, 2)

def dynamic_priority(p, current_time):
    waiting = current_time - p.arrival
    waiting_score = min(waiting, 5)

    short_burst_score = min((1 / p.remaining) * 4, 2)

    io_boost = 3 if p.io_bound else 0
    fg_boost = 3 if p.foreground else 0
    energy_penalty = estimate_energy(p.burst)

    priority_value = (
        p.priority * 2 +
        waiting_score +
        short_burst_score +
        io_boost +
        fg_boost -
        energy_penalty
    )

    return round(priority_value, 2)


def cadps(processes):
    time = 0
    completed = []
    ready = []
    timeline = []

    context_snapshot = {}  # NEW

    processes.sort(key=lambda p: p.arrival)

    while processes or ready:
        while processes and processes[0].arrival <= time:
            ready.append(processes.pop(0))

        if ready:
            # recalculate dynamic priorities
            priorities = {
                p: dynamic_priority(p, time)
                for p in ready
            }

            # save context snapshot (latest values)
            context_snapshot = {}
            for p, dp in priorities.items():
                context_snapshot[f"P{p.pid}"] = {
                    "waiting": time - p.arrival,
                    "remaining": p.remaining,
                    "cpu_usage": estimate_cpu_usage(p.burst),
                    "energy": estimate_energy(p.burst),
                    "io": "Yes" if p.io_bound else "No",
                    "fg": "Yes" if p.foreground else "No",
                    "dynamic_priority": dp
                }

            # select highest priority process
            p = max(priorities, key=priorities.get)

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
    result["context"] = context_snapshot  # NEW
    return result
