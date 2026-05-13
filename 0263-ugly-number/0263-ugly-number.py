class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for prime in [2, 3, 5]:     # divide by 2 then 3 then 5
            while n % prime == 0:   # keep dividing as long as this prime divides evenly
                n //= prime         # integer divide
        return n == 1               # fully divided by 2 / 3 / 5 and return boolean


# Time Complexity   : O(log n)
# Space Complexity  : O(1)
# by ar-sayeem [May 13, 2026]
