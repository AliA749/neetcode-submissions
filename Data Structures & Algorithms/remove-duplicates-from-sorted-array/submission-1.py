class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=nums[0]
        for i in nums[1:]:
            if i==index:
                nums.remove(i)
            else:
                index=i
        k=len(nums)
        return k

