class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted((val, i) for i, val in enumerate(nums))
        indexL=0
        indexR=(len(nums)-1)
        left=sorted_nums[indexL][0]
        right=sorted_nums[indexR][0]
        sum_found=False
        while sum_found==False:
            if left + right < target:
                indexL+=1
                left=sorted_nums[indexL][0]
            elif left + right > target:
                indexR-=1
                right=sorted_nums[indexR][0]
            else:
                res = sorted([sorted_nums[indexL][1], sorted_nums[indexR][1]])
                newlist=[res[0], res[1]]
                sum_found=True
        return newlist
