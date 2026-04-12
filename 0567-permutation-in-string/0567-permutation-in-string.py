class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):   # s1 can't fit in s2
            return False
        
        count1 = [0] * 26   # lower case a-z, size of 26
        count2 = [0] * 26

        for char in s1:
            count1[ord(char) - ord('a')] += 1

        for i in range(len(s1)):
            count2[ord(s2[i]) - ord('a')] += 1

        if count1 == count2:
            return True

        for i in range(len(s1), len(s2)):   # range(a, b) means start at a, stop before b
            count2[ord(s2[i]) - ord('a')] += 1
            count2[ord(s2[i - len(s1)]) - ord('a')] -= 1     # aves the window from the left → remove it
            if count1 == count2:
                return True
                
        return False


# Time Complexity: O(n)
# Space Complexity: O(1)
# by ar-sayeem [April 12, 2026]