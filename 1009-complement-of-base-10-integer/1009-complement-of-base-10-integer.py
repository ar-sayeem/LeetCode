class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        bit_len = n.bit_length()    # count bit length of integer
        mask = (1 << bit_len) - 1   # makw an all 1s mask
        return n ^ mask             # flip n with XOR -> 101 ^ 111 = 010 = 2

# Time Complexity: O(log N)
# Space Complexity: O(1)
# by ar-sayeem [March 11, 2026]