# currentSum += arr[i] - arr[i-k]
# This commented line hints at the sliding window technique used to efficiently update the sum.

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Initialize a counter to keep track of the number of valid subarrays.
        count = 0
        # Calculate the sum of the first subarray of size k.
        currentSum = sum(arr[:k])
        # Calculate the average of the first subarray.
        avgSum = currentSum / k

        # Check if the average of the first subarray meets the threshold.
        if avgSum >= threshold:
            # If it does, increment the count.
            count += 1

        # Iterate through the rest of the array using a sliding window of size k.
        for i in range(k, len(arr)):
            # Efficiently update the current sum by subtracting the element that is leaving the window
            # (arr[i-k]) and adding the new element entering the window (arr[i]).
            currentSum += arr[i] - arr[i - k]
            # Calculate the average of the current window.
            avgSum = currentSum / k
            # Check if the average of the current subarray meets the threshold.
            if avgSum >= threshold:
                # If it does, increment the count.
                count += 1

        # Return the total count of subarrays that satisfy the condition.
        return count