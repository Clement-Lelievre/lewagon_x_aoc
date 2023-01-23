INPUT = """Step T must be finished before step C can begin.
Step V must be finished before step C can begin.
Step Y must be finished before step H can begin.
Step R must be finished before step U can begin.
Step B must be finished before step J can begin.
Step Q must be finished before step O can begin.
Step W must be finished before step O can begin.
Step S must be finished before step X can begin.
Step I must be finished before step N can begin.
Step X must be finished before step H can begin.
Step M must be finished before step L can begin.
Step A must be finished before step F can begin.
Step G must be finished before step P can begin.
Step U must be finished before step E can begin.
Step Z must be finished before step E can begin.
Step H must be finished before step L can begin.
Step P must be finished before step C can begin.
Step K must be finished before step F can begin.
Step O must be finished before step C can begin.
Step C must be finished before step F can begin.
Step D must be finished before step L can begin.
Step L must be finished before step F can begin.
Step N must be finished before step E can begin.
Step J must be finished before step F can begin.
Step F must be finished before step E can begin.
Step I must be finished before step A can begin.
Step Z must be finished before step J can begin.
Step I must be finished before step P can begin.
Step T must be finished before step E can begin.
Step R must be finished before step F can begin.
Step U must be finished before step H can begin.
Step K must be finished before step E can begin.
Step D must be finished before step N can begin.
Step U must be finished before step C can begin.
Step D must be finished before step J can begin.
Step N must be finished before step F can begin.
Step C must be finished before step J can begin.
Step U must be finished before step J can begin.
Step A must be finished before step O can begin.
Step H must be finished before step N can begin.
Step P must be finished before step O can begin.
Step I must be finished before step E can begin.
Step G must be finished before step F can begin.
Step O must be finished before step J can begin.
Step Q must be finished before step F can begin.
Step G must be finished before step J can begin.
Step X must be finished before step E can begin.
Step S must be finished before step D can begin.
Step R must be finished before step P can begin.
Step K must be finished before step L can begin.
Step R must be finished before step Q can begin.
Step L must be finished before step N can begin.
Step Q must be finished before step C can begin.
Step C must be finished before step D can begin.
Step C must be finished before step N can begin.
Step O must be finished before step E can begin.
Step W must be finished before step F can begin.
Step K must be finished before step D can begin.
Step T must be finished before step H can begin.
Step M must be finished before step D can begin.
Step Y must be finished before step Z can begin.
Step J must be finished before step E can begin.
Step S must be finished before step F can begin.
Step G must be finished before step U can begin.
Step V must be finished before step S can begin.
Step Y must be finished before step F can begin.
Step G must be finished before step H can begin.
Step T must be finished before step Q can begin.
Step S must be finished before step U can begin.
Step V must be finished before step D can begin.
Step W must be finished before step M can begin.
Step M must be finished before step E can begin.
Step A must be finished before step H can begin.
Step B must be finished before step F can begin.
Step B must be finished before step N can begin.
Step D must be finished before step F can begin.
Step W must be finished before step K can begin.
Step P must be finished before step E can begin.
Step B must be finished before step X can begin.
Step Q must be finished before step U can begin.
Step Q must be finished before step X can begin.
Step X must be finished before step N can begin.
Step M must be finished before step Z can begin.
Step G must be finished before step Z can begin.
Step S must be finished before step G can begin.
Step P must be finished before step F can begin.
Step I must be finished before step O can begin.
Step R must be finished before step A can begin.
Step L must be finished before step J can begin.
Step B must be finished before step I can begin.
Step C must be finished before step E can begin.
Step B must be finished before step W can begin.
Step P must be finished before step N can begin.
Step H must be finished before step C can begin.
Step K must be finished before step J can begin.
Step Y must be finished before step M can begin.
Step Z must be finished before step P can begin.
Step I must be finished before step K can begin.
Step V must be finished before step E can begin.
Step Y must be finished before step P can begin.
Step T must be finished before step R can begin.
"""

inp = [e for e in INPUT.splitlines() if e]
steps = set(row[5] for row in inp).union((not_first := set(row[-12] for row in inp)))
seq = ""
steps_done = set()
steps_requirements = {
    step: set([row[5] for row in inp if row[-12] == step]) for step in steps
}

for i in range(len(steps)):
    candidates = [
        k for k in steps_requirements if steps_requirements[k].issubset(steps_done)
    ]
    seq += (s := sorted(candidates)[0])
    steps_done.add(s)
    steps_requirements.pop(s)
print(seq)

# part 2
durations = dict(zip(sorted(seq), range(61, 61 + len(seq))))
steps_done = set()
steps_requirements = {
    step: set([row[5] for row in inp if row[-12] == step]) for step in steps
}
workers = 5
workers_status = {
    i: 0 for i in range(workers)
}  # values are the time in seconds needed before they are available (0 means they're available)
seq = ""
time = 0
steps_in_pipe = []

while len(seq) < len(steps):
    # print(f'{steps_done=}')

    for elf in workers_status:  # check if a step has finished
        if workers_status[elf] == 1:
            steps_done.add(
                (done_step := [elem[1] for elem in steps_in_pipe if elem[0] == elf][0])
            )
            seq += done_step
            steps_in_pipe.remove([elem for elem in steps_in_pipe if elem[0] == elf][0])
            # print(f'{seq=}, {workers_status=}')

    workers_status = {
        k: max(0, v - 1) for k, v in workers_status.items()
    }  # account for time spent: decrement 1 sec
    candidates = sorted(
        k for k in steps_requirements if steps_requirements[k].issubset(steps_done)
    )
    if candidates and (
        ready_workers := {k: v for k, v in workers_status.items() if v == 0}
    ):  # see if some new work can be assigned
        nb_tasks_todo = min(len(candidates), len(ready_workers))
        # print('found work!')
        i = 0
        for task, task_duration in zip(
            {
                worker_nb: duration
                for worker_nb, duration in workers_status.items()
                if duration == 0
            }.keys(),
            {
                step: duration
                for step, duration in durations.items()
                if step in candidates
            }.values(),
        ):
            workers_status[task] += task_duration
            steps_requirements.pop(candidates[i])
            steps_in_pipe.append((task, candidates[i]))
            # print(f'{workers_status=}')
            i += 1
    if len(seq) < len(steps):
        time += 1


print(time)
