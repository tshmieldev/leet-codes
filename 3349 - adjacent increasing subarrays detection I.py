class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def isIncreasing(arr):
            if len(arr) < 2:
                return True
            for i in range(1, len(arr)):
                if arr[i] <= arr[i-1]:
                    return False
            return True
        for i in range(len(nums)-k*2+1):
            if isIncreasing(nums[i:k+i]) and isIncreasing(nums[k+i:k+i+k]):
                return True
        return False