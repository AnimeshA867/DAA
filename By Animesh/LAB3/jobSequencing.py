import time

class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs, t):
    n = len(jobs)
    jobs.sort(key=lambda x: x.profit, reverse=True)
    result = [False] * t
    job_sequence = ['-1'] * t
    for i in range(n):
        for j in range(min(t-1, jobs[i].deadline-1), -1, -1):
            if result[j] is False:
                result[j] = True
                job_sequence[j] = jobs[i].id
                break
    return job_sequence

# Input jobs with deadlines and profits
jobs = [Job('a', 2, 100), Job('b', 1, 19), Job('c', 2, 27), Job('d', 1, 25), Job('e', 3, 15)]
t = 3

# Measure the time taken to execute the Job Sequencing function
start_time = time.time()
sequence = job_sequencing(jobs, t)
end_time = time.time()

# Output the result and time taken
print("Job sequence to maximize profit:", sequence)
print(f"Time taken to execute the Job Sequencing program: {end_time - start_time:.6f} seconds")
print("Program by Animesh")
