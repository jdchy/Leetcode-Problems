class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return True if s in re.findall(p, s) else False