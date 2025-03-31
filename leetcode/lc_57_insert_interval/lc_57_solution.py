class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # If the list of intervals is empty, just return the new interval as the only interval
        if not intervals: 
            return [newInterval]
        
        result = []

        # Iterate over each interval
        for i in range(0, len(intervals)):
            # Case 1: New interval comes completely before the current interval
            # Since intervals are sorted, we can insert the new interval and append the rest
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            
            # Case 2: New interval overlaps with the current interval
            # Merge the overlapping intervals by taking the min of starts and max of ends
            elif newInterval[0] <= intervals[i][1] and newInterval[1] >= intervals[i][0]:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                newInterval = [newInterval[0], newInterval[1]]
            # Case 3: Current interval is completely before the new interval
            # No overlap and new interval comes later, so we add the current interval as it is
            else:
                result.append(intervals[i])
        
        # If we finish iterating, and the newInterval hasn't been added yet (it might be after all intervals)
        result.append(newInterval)
        return result



        