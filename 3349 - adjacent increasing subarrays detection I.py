class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(1, len(nums) - 2):
            if nums[i] > nums[i-1] and nums[i+1] < nums[i] and nums[i+2] > nums[i+1]:
                return True
        return False