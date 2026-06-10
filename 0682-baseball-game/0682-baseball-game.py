class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []

        for op in operations:
            if op == '+':
                stk.append(stk[-1] + stk[-2])
            elif op == 'D':
                stk.append(int(stk[-1]) * 2)
            elif op == 'C':
                stk.pop()
            else:
                stk.append(int(op))

        return sum(stk)


# Time Complexity   : O(N)
# Space Complexity  : O(N)
# by ar-sayeem [June 10, 2026]