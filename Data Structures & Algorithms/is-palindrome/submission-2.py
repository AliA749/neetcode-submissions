class Solution:
    def isPalindrome(self, s: str) -> bool:
        punc_marks={".","?","!","'",","," ",":"}
        strings=s.lower()
        for mark in punc_marks:
            strings=strings.replace(mark,"")
        reverseds=strings[::-1]
        return strings==reverseds    