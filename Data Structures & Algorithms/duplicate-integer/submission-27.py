class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) == 1:
            return False
        for i in range(0,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False