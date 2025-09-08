class Solution(object):
    def removeDuplicates(self, nums):
        l = 0
        r = 1
        if len(nums) < 2:
            return len(nums)
        while r < len(nums):
            
            if nums[l] != nums[r]:
                # valid
                l += 1
                nums[l] = nums[r]
                r += 1
            else:
                r += 1

            
        return l + 1
        