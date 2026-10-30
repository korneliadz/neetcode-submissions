class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def ch(string : str):
            return sorted(string)
        return ch(s) == ch(t)
        