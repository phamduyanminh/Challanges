class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sorting intervals based on the start index of each interval
        intervals.sort(key = lambda interval: interval[0])

        # Initialize result with the first interval
        result = [intervals[0]]

        # Start iterating from the interval at index 1
        for currentStart, currentEnd in intervals[1:]:
            # Get the end of the last interval in the result
            latestEnd = result[-1][1]

            # If the current interval's start is less than or equal to latestEnd,
            # it overlaps with the last interval in result
            if currentStart <= latestEnd:
                # Merge the overlapping intervals by updating the end
                result[-1][1] = max(latestEnd, currentEnd)
            else:
                # No overlap; append the current interval as it is
                result.append([currentStart, currentEnd])
        
        return result

            

        