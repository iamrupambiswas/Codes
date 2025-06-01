def job_sequencing(deadlines, profits):
    """
    Greedy Approach to the Job Sequencing Problem.

    Idea:
    - Pair up each job's deadline and profit.
    - Sort all jobs by profit in descending order — greedily try to take the highest profit jobs first.
    - For each job, try to schedule it on the latest available slot before or on its deadline.
      If that slot is taken, look for an earlier one.
    - Use a dictionary to track used time slots.
    - Return total number of jobs done and the accumulated profit.
    """

    # Pair each job's deadline with its profit
    jobs = [(deadlines[i], profits[i]) for i in range(len(profits))]

    # Sort jobs by profit in descending order (greedy step)
    jobs.sort(key=lambda x: x[1], reverse=True)

    # Dictionary to store which time slots have been filled with a job
    schedule = {}

    # Iterate through each job in order of profit
    for deadline, profit in jobs:
        # Try to schedule the job at its deadline or the closest earlier free slot
        for slot in range(deadline, 0, -1):
            if slot not in schedule:
                schedule[slot] = profit  # Assign job to the slot
                break  # Move to the next job after scheduling

    # Calculate total profit and number of jobs successfully scheduled
    total_jobs = len(schedule)
    total_profit = sum(schedule.values())

    return [total_jobs, total_profit]


# Test case
print(job_sequencing([4, 1, 1, 1], [20, 10, 40, 30]))
