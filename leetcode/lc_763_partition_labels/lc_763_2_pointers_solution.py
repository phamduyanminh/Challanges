class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []

        # 'start' contains the beginning index of the current partition
        start = 0
        
        # Iterating through entire string
        while start < len(s):
            # 'end' is set to the last occurrence of the first character of the current partition
            end = s.rfind(s[start])
            # 'currentIndex' is used to scan through characters in the current partition
            currentIndex = start

            # Move through the current partition to ensure every character's last occurrence is included
            while currentIndex < end:
                # For each character, update 'end' if its last occurrence is further to the right
                end = max(end, s.rfind(s[currentIndex]))
                 # Move to the next character in the current partition
                currentIndex += 1
            
            # When currentIndex reaches end, we have a complete partition
            # The size of the partition is calculated as (end - start + 1)
            result.append(end+1-start)

            # Move 'start' to the beginning of the next partition
            start = end+1
        
        return result
            



