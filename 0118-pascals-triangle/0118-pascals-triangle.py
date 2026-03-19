class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result
        result.append([1])
        if numRows == 1:
            return result
        
        for i in range(1, numRows):
            prev_row = result[i - 1]
            row  = [1]

            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
            result.append(row)
        return result


# Time Complexity: O(N²)
# Space Complexity: O(N²)
# by ar-sayeem [March 19, 2026]