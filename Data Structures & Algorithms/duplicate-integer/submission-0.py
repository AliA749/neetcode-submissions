class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       hashnums = set(nums)
       return len(hashnums)!=len(nums)         