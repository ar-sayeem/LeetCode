class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False

        half = 0
        while(x > half):                    # half(0)   ---   x(121)
            half = (half * 10) + (x % 10)   # (0 * 10) + (121 % 10) -> 1
            x = x // 10                     # 121 // 10 -> 12

        return x == half or x == half // 10
        #       (for even)    (12 == 121 // 10 -> 12)

        """
        2nd Iteration:
        half(1)   ---   x(12)
        (1 * 10) + (12 % 10) -> 12
        12 // 10 -> 1

        NOW, [x -> 1] && [half == (half // 10) == (12 // 10) -> 1] Therefore, 121 is Palindrome

        3rd Iteration:
        half(12)   ---   x(1)
        (12 * 10) + (1 % 10) -> 120
        1 // 10 -> 0

        """