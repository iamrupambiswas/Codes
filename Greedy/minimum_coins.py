"""
minimum_coins.py

Description:
    A simple Python script to determine the minimum number of currency coins/notes 
    required to sum up to a given amount using a greedy approach.

Approach:
    - Validate input (must be a positive integer).
    - Use a greedy algorithm: always use the largest denomination first.
    - Subtract the value and continue with the remainder.
    - Return a list of coins/notes used.

Usage:
    Run this script directly or import the `minimum_coins` function into another module.
"""

def minimum_coins(n):
    try:
        # --- Input Validation ---
        if not isinstance(n, int):
            raise ValueError("Input value has to be an integer!")
        if n <= 0:
            raise ValueError("Input value can't be 0 or less!")

        # --- Greedy Approach using Indian Currency Denominations ---
        denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
        ans = []

        for coin in denominations:
            if n >= coin:
                count = n // coin
                n %= coin
                ans.extend([coin] * count)  # Add the coin `count` times

        return ans

    except Exception as e:
        print(f"Exception occurred: {e}")
        return 0

# --- Example Usage ---
if __name__ == "__main__":
    amount = 49
    result = minimum_coins(amount)
    print(f"Minimum coins/notes for â‚¹{amount}: {result}")
