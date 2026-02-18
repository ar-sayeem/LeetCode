class Solution:
    def isSameAfterReversals(self, num: int) -> bool:

        # If number ends with 0 → it will change
        # Except if the number is 0 itself
        return (num == 0 or (num % 10 != 0))


        # str(n) converts the number to a string.
        # [::-1] reverses the string.
        # int() converts the reversed string back to a number.

        # r1 = int(str(num)[::-1])
        # r2 = int(str(r1)[::-1])
        # return (r2 == num)

# Time Complexity: O(n)
# Space Complexity: O(n)
# by ar-sayeem [February 19, 2026]