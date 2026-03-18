class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        sumCountMap = defaultdict(int)      # sum   |   count
        sumCountMap[0] = 1                  #  0    |     1

        result = 0
        prefixSum = 0

        for i in nums:
            prefixSum += i
            if prefixSum - k in sumCountMap:
                result += sumCountMap[prefixSum - k]
            
            sumCountMap[prefixSum] += 1
        
        return result
    

# Time Complexity: O(N)
# Space Complexity: O(N)
# by ar-sayeem [March 18, 2026]




        # N = len(nums)
        # count = 0
        # for i in range(N):      # loop 0 to N
        #     prefixSum = 0
        #     for j in range(i, N):   # loop i to N
        #         prefixSum += nums[j]
        #         if prefixSum == k:
        #             count += 1
        # return count
