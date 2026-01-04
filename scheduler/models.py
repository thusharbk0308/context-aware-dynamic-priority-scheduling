class Process:
    def __init__(self, pid, arrival, burst, priority,
                 io_bound=False, foreground=False):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.remaining = burst
        self.priority = priority

        self.io_bound = io_bound
        self.foreground = foreground

        # Metrics
        self.start_time = None
        self.completion_time = None
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = None
        self.starved = False
