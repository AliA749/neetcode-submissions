class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        firstin =0
        for i in range(len(nums)):
           if nums[i] != val:
            nums[firstin]= nums[i]
            firstin+=1
                
        return firstin        
        