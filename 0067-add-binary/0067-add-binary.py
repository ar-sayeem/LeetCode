class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return bin(int(a, 2) + int(b, 2))[2:]

        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digitA + digitB + carry
            res = str(total % 2) + res
            carry = total // 2

        if carry:
            res = "1" + res

        return res


# Time Complexity: O(n)
# Space Complexity: O(n)
# by ar-sayeem [January 30, 2026]
