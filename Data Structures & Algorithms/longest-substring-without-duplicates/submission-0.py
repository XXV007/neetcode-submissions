class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last index of each character
        char_index = {}
        max_length = 0
        left = 0

        # Iterate over the string with the right pointer
        for right in range(len(s)):
            # If character is seen and is inside the current window
            if s[right] in char_index and char_index[s[right]] >= left:
                # Move left pointer past the previous occurrence
                left = char_index[s[right]] + 1
            # Update the last seen index of the character
            char_index[s[right]] = right
            # Update max_length if current window is larger
            max_length = max(max_length, right - left + 1)
        
        return max_length
        