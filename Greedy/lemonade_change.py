def lemonade_change(bills):
    try:
        # Input validation
        if not bills:
            raise ValueError("Input list can't be empty!")
        if any(b <= 0 for b in bills):
            raise ValueError("All bills must be positive!")

        # Helper hashmap to store available change
        change = {5: 0, 10: 0}

        for bill in bills:
            if bill == 5:
                change[5] += 1
            elif bill == 10:
                if change[5] > 0:
                    change[5] -= 1
                    change[10] += 1
                else:
                    return False
            elif bill == 20:
                if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False
            else:
                raise ValueError(f"Invalid bill amount: {bill}")

        return True

    except Exception as e:
        print(f"Exception occurred: {e}")
        return False


# Example usage
if __name__ == "__main__":
    print(lemonade_change([5, 5, 5, 10, 20, 20]))  # Should return False
