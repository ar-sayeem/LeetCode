class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        # if n == 0:
        #     return 0

        for i in range(32):
            result <<= 1  # make 1 bit space for result by left shifting
            result |= n & 1
            # retult = result | (n & 1)
            # (n & 1) -> find the LSB
            # result =| LSB -> using OR to append the LSB at the end of result

            n >>= 1  # now that LSB of n added in result right shift to get new LSB

        return result


# Time Complexity: O(1)
# Space Complexity: O(1)
# by ar-sayeem [February 16, 2026]
