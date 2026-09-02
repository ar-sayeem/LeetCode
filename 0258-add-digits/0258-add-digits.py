class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0    # edge case
        
        # for all other numbers
        return 1 + (num - 1) % 9

# Time Complexity   : O()
# Space Complexity  : O()
# by ar-sayeem [September 02, 2026]