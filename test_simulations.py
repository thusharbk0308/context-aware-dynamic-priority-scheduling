from scheduler.models import Process
from scheduler.fcfs import fcfs
from scheduler.sjf import sjf
from scheduler.priority import priority_scheduling
from scheduler.round_robin import round_robin
from scheduler.cadps import cadps
import copy

processes = [
    Process(1, 0, 6, 2, io_bound=True, foreground=True),
    Process(2, 2, 4, 1),
    Process(3, 4, 8, 3, foreground=True),
    Process(4, 6, 5, 2, io_bound=True),
]

algorithms = {
    "FCFS": fcfs,
    "SJF": sjf,
    "Priority": priority_scheduling,
    "Round Robin": round_robin,
    "CADPS": cadps
}

for name, algo in algorithms.items():
    result = algo(copy.deepcopy(processes))
    print(name, result)
