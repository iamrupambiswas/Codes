def fractional_knapsack(values, weights, capacity):
    """
    Solves the fractional knapsack problem.
    
    Args:
        values (list of float): The values of the items.
        weights (list of float): The weights of the items.
        capacity (float): The total capacity of the knapsack.
        
    Returns:
        float: The maximum total value that can be carried.
    """
    try:
        # Input validation
        if not values or not weights:
            raise ValueError("Input lists cannot be empty.")
        if len(values) != len(weights):
            raise ValueError("Values and weights lists must have the same length.")
        if capacity < 0:
            raise ValueError("Capacity cannot be negative.")

        # Calculate value-to-weight ratios and sort by descending ratio
        items = [(values[i] / weights[i], values[i], weights[i]) for i in range(len(values))]
        items.sort(reverse=True)

        total_value = 0.0

        for ratio, value, weight in items:
            if weight <= capacity:
                total_value += value
                capacity -= weight
            else:
                total_value += ratio * capacity
                break  # knapsack is full

        return total_value

    except ZeroDivisionError:
        print("Error: Item weight cannot be zero.")
        return 0.0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0.0


# Example usage
if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    knapsack_capacity = 50

    result = fractional_knapsack(values, weights, knapsack_capacity)
    print(f"Maximum value in the knapsack: {result}")
