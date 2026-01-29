class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Reverse in-place (no extra list)
        digits.reverse()

        carry = 1
        i = 0

        while carry:  # carry == 1
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                digits.append(1)
                carry = 0
            i += 1

        # Reverse back in-place
        digits.reverse()
        return digits


# Time Complexity: O(n)
# Space Complexity: O(1)
# by ar-sayeem [January 29, 2026]
