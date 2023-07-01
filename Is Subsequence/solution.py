class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        obj = iter(t)
        return all(c in obj for c in s)