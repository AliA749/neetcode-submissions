class Solution:
    def isValid(self, s: str) -> bool:
        stack=list()
        matched={"}":"{", ")":"(", "]":"["}
        for i in s:
            if i in matched.values():
                stack.append(i)
            else:
                if not stack or stack[-1] != matched[i]:
                    return False
                stack.pop()
        return len(stack)==0




