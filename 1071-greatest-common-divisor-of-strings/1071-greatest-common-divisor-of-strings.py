class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Helper function to check if str1 can be formed by repeating str2
        def is_divisible(s: str, t: str) -> bool:
            if len(s) % len(t) != 0:
                return False
            return s == t * (len(s) // len(t))
        
        # Finding the greatest common divisor of lengths of str1 and str2
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a
        
        # Calculate the gcd of the lengths of str1 and str2
        len_gcd = gcd(len(str1), len(str2))
        
        # Candidate for the gcd string
        candidate = str1[:len_gcd]
        
        # Check if candidate can divide both str1 and str2
        if is_divisible(str1, candidate) and is_divisible(str2, candidate):
            return candidate
        else:
            return ""