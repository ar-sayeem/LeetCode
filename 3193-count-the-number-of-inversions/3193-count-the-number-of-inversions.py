class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10**9 + 7  # take modulo every step to avoid overflow

        req_map = {end: cnt for end, cnt in requirements}  # O(1) lookup for requirements

        if req_map.get(0, 0) != 0:  # index 0 can never have inversions
            return 0

        max_inv = max(req_map.values())  # no need to track beyond max required inversions

        prev = [0] * (max_inv + 1)
        prev[0] = 1  # base case: 1 element, 0 inversions, 1 way

        for i in range(1, n):  # place elements one by one
            curr = [0] * (max_inv + 1)  # fresh row for current prefix

            for j in range(max_inv + 1):
                if j > 0:
                    curr[j] = curr[j - 1]               # carry forward running window total
                curr[j] = (curr[j] + prev[j]) % MOD     # add new term entering the window
                fell_off = j - i - 1
                if fell_off >= 0:
                    curr[j] = (curr[j] - prev[fell_off] + MOD) % MOD  # subtract term leaving the window

            if i in req_map:  # checkpoint: enforce exact inversion count
                required = req_map[i]
                keep = curr[required]
                curr = [0] * (max_inv + 1)
                curr[required] = keep  # zero out everything except required count

            prev = curr  # slide forward, discard old row

        return prev[req_map[n - 1]]  # answer is at the last required inversion count


# Time Complexity: O(N x M)
# Space Complexity: O(M)
# by ar-sayeem [March 20, 2026]