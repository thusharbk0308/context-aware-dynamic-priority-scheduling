def calculate_metrics(processes):
    total_wait = 0
    total_turnaround = 0
    total_response = 0
    starvation_count = 0

    for p in processes:
        p.turnaround_time = p.completion_time - p.arrival
        p.waiting_time = p.turnaround_time - p.burst

        if p.response_time is None:
            p.response_time = p.start_time - p.arrival

        total_wait += p.waiting_time
        total_turnaround += p.turnaround_time
        total_response += p.response_time

        # starvation rule (academic assumption)
        if p.waiting_time > 2 * p.burst:
            p.starved = True
            starvation_count += 1

    n = len(processes)
    return {
        "avg_waiting_time": total_wait / n,
        "avg_turnaround_time": total_turnaround / n,
        "avg_response_time": total_response / n,
        "starvation_count": starvation_count
    }
