class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length= len(nums)
        holder=[1]*length
        prefix=1
        for i in range(length):
            holder[i]=prefix
            prefix*=nums[i]
        suffix = 1
        for i in range(length-1,-1,-1):
            holder[i]*=suffix
            suffix*=nums[i]
        return holder