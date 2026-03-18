from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        sumCountMap = defaultdict(int)      # sum   |   count
        sumCountMap[0] = 1                  #  0    |     1

        result = 0
        prefixSum = 0

        for i in nums:
            prefixSum += i                              # move one step forward
            if prefixSum - k in sumCountMap:            # did we see this before?
                result += sumCountMap[prefixSum - k]    # yes! count those subarrays
            sumCountMap[prefixSum] += 1                 # record this stop in notebook
        
        return result


# Time Complexity: O(N)
# Space Complexity: O(N)
# by ar-sayeem [March 18, 2026]