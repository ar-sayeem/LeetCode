class Solution:
    def isHappy(self, n: int) -> bool:

        def nextNum(num):
            # sum of each digit
            return sum(int(d)**2 for d in str(num))
        
        slow = n
        fast = nextNum(n)

        while fast != 1 and slow != fast:
            slow = nextNum(slow)            # 1 step
            fast = nextNum(nextNum(fast))   # 2 step

        return fast == 1    # boolean

# Time Complexity   : O(logN)
# Space Complexity  : O(1)
# by ar-sayeem [May 12,2026]