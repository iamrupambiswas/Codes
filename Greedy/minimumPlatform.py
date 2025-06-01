class Solution:
    def minimumPlatform(self, arrival_times, departure_times):
        """
        Given arrival and departure times of trains, this function returns
        the minimum number of platforms required at a railway station so that
        no train has to wait.

        Approach:
        - We treat each arrival and departure as an event.
        - Combine and sort all events based on time.
        - Traverse through events, incrementing count on arrival and decrementing on departure.
        - Track the maximum number of platforms needed at any time.

        Time Complexity: O(n log n) -> due to sorting the events.
        Space Complexity: O(n) -> for storing the events list.
        """
        # Step 1: Mark each arrival with 'A' and departure with 'D'
        events = [(time, 'A') for time in arrival_times]
        events += [(time, 'D') for time in departure_times]

        # Step 2: Sort events. If time is the same, arrivals come before departures
        events.sort()

        current_platforms = 0  # Tracks platforms needed at the current time
        max_platforms = 0      # Stores the result - max platforms needed

        # Step 3: Traverse events and update counters
        for time, event_type in events:
            if event_type == 'A':
                current_platforms += 1
            else:
                current_platforms -= 1

            max_platforms = max(max_platforms, current_platforms)

        return max_platforms


#Added minimumPlatform solution using event-based sweep line approach