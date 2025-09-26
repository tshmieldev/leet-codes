class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        c = 0
        nums.sort()

        for biggest in range(len(nums)-1, 1, -1):
            l = 0
            r = biggest - 1
            while l < r:
                if nums[l] + nums[r] > nums[biggest]:
                    c += r-l
                    r -= 1
                else:
                    l += 1

        return c