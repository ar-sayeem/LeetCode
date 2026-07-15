class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # Sum of first n odd numbers = 1 + 3 + ... + (2n-1) = n^2
        # Sum of first n even numbers = 2 + 4 + ... + 2n = n*(n+1)
        
        # We need gcd(n^2, n*(n+1))
        # Both terms share a common factor of n, so factor it out:
        # gcd(n^2, n*(n+1)) = n * gcd(n, n+1)
        
        # n and n+1 are consecutive integers, so they are always coprime
        # gcd(n, n+1) = 1
        
        # Therefore, gcd(n^2, n*(n+1)) = n * 1 = n
        return n

# Time Complexity   : O(1)
# Space Complexity  : O(1)
# by ar-sayeem [July 15, 2026]