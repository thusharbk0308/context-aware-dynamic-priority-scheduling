from flask import Flask, render_template, request
import copy

from scheduler.models import Process
from scheduler.fcfs import fcfs
from scheduler.sjf import sjf
from scheduler.priority import priority_scheduling
from scheduler.round_robin import round_robin
from scheduler.cadps import cadps

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    n = 4  # fixed

    if request.method == "POST":
        processes = []

        for i in range(n):
            processes.append(
                Process(
                    pid=i + 1,
                    arrival=int(request.form[f"arrival{i}"]),
                    burst=int(request.form[f"burst{i}"]),
                    priority=int(request.form[f"priority{i}"]),
                    io_bound=True if request.form.get(f"io{i}") else False,
                    foreground=True if request.form.get(f"fg{i}") else False,
                )
            )

        algorithms = {
            "FCFS": fcfs,
            "SJF": sjf,
            "Priority": priority_scheduling,
            "Round Robin": round_robin,
            "CADPS": cadps
        }

        results = {}
        for name, algo in algorithms.items():
            results[name] = algo(copy.deepcopy(processes))

    return render_template(
        "index.html",
        results=results,
        form_data=request.form
    )

if __name__ == "__main__":
    app.run(debug=True)
