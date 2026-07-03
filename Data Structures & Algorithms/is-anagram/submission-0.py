class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorteds,sortedt= sorted(list(s)),sorted(list(t))
        if sorteds == sortedt:
            return True
        return False