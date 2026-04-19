from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)        # missing key? auto → []

        for word in strs:                       # iterate each word
            count = [0] * 26                    # fresh 26-slot counter per word
            for char in word:                   # iterate each character
                count[ord(char) - ord("a")] += 1  # map char → index 0-25, increment

            key = tuple(count)                  # list → hashable tuple (dict key)
            anagram_dict[key].append(word)      # same key = same anagram bucket

        return list(anagram_dict.values())      # return all grouped buckets


# Time Complexity   : O(N * K)
# Space Complexity  : O(N * K)
# by ar-sayeem [April 19, 2026]