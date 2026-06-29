class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for i in patterns:
            if i in word:
                count += 1
        return count

# Time Complexity   : O(k × n × m)
# Space Complexity  : O(1)
# by ar-sayeem [June 29, 2026]