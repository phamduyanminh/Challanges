class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Create an empty dictionary to store the last appearance index of each character
        hashMap = {}

         # Returns key-value pairs (char-index) as we iterate through the string.
        for index, char in enumerate(s):
            hashMap[char] = index

        result = []
        currentSize = 0 # Counter for the size of the current partition 
        currentEnd = 0 # Track the farthest index we need to go in the current partition

        # Iterate through the string a second time using enumerate() to get both the index and character
        for index, char in enumerate(s):
            # Increase the size of the current partition
            currentSize += 1

            # Extend the partition's end if this character's last occurrence is larger than the currentEnd
            currentEnd = max(currentEnd, hashMap[char])

            # When the current index matches the current partition end,
            # it means we've included all characters that appear in this partition
            if index == currentEnd:
                # Append the size of the current partition to the result
                result.append(currentSize)
                # Reset the partition size counter for the next partition
                currentSize = 0
        
        return result
            


