class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s = set(ransomNote)
        
        for mag in magazine:
            if mag in s:
                return True