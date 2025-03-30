class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []

        # Use a dictionary to store the last index place for every letter
        hashmap = {}
        for index, char in enumerate(s):
            hashmap[char] = index
        
        start = 0
        end = 0
        
        for index, char in enumerate(s):
            # Update 'end' with the furthest last index for current letter in the current partition
            end = max(end, hashmap[char])

            # When the current index matches the current partition end,
            # it means we've included all characters that appear in this partition
            if index == end:
                result.append(end+1-start)
                start = index+1

        return result
            



