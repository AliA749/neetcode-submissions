class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorteds,sortedt= sorted(s),sorted(t)
        if len(s) != len(t):
            return False
        return sorteds == sortedt