class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_divisible(s: str, t: str) -> bool:
            if len(s) % len(t) != 0:
                return False
            return s == t * (len(s) // len(t))
        
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a
        
        len_gcd = gcd(len(str1), len(str2))
        
        candidate = str1[:len_gcd]
        
        if is_divisible(str1, candidate) and is_divisible(str2, candidate):
            return candidate
        else:
            return ""