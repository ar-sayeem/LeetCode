class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += 1
            n &= n - 1  # remove the last 1 in the number

        return count


# Time Complexity: O(m)     m = number of 1 bits in n
# Space Complexity: O(1)
# by ar-sayeem [February 17, 2026]


        # return bin(n).count('1')

        # # bin(11) returns  -> "0b1011"
        # # bin(n)[2:] returns -> "1011"
        # # 0 = argument index, b = binary formatting

        # # T -> O(k)  |  S -> O(K)
        # # k = number of bits in n
