class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        largest = 0
        charSet = set()

        for right in range(n):              # loop till end of string
            while s[right] in charSet:
                charSet.remove(s[left])     # remove left char from charSet
                left += 1                   # shift l to right 1 step
                
            length = (right - left) + 1     # length of unique subString
            charSet.add(s[right])           # add the right char to charSet
            largest = max(largest, length)
        return largest
    

# Time Complexity: O(N)
# Space Complexity: O(N)
# by ar-sayeem [March 02, 2026]