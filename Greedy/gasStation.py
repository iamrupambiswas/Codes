def canCompleteCircuit(gas, cost):
    """
    Greedy approach to find the starting gas station index from where the car can complete the circuit.

    Idea:
    - If total gas is less than total cost, it's impossible to complete the circuit.
    - Otherwise, try to find a valid starting point where running total never goes negative.
    - If at any point currentGas < 0, reset the start to the next station (i+1),
      because the current segment can't be completed from the current start.
    """

    totalGas = sum(gas)
    totalCost = sum(cost)

    # Check if the journey is possible at all
    if totalGas < totalCost:
        return -1

    currentGas = 0  # Running fuel balance
    start = 0       # Index of starting station

    for i in range(len(gas)):
        currentGas += gas[i] - cost[i]

        # If we run out of gas, reset start to the next station
        if currentGas < 0:
            start = i + 1
            currentGas = 0

    return start
