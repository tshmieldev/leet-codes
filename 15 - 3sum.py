class Solution(object):
    def twoSum(self, nums, target):
        # assume nums is sorted
        l = 0
        r = len(nums) - 1

        if r < 1:
            return []
        solutions = []
        while l < r:
            suma = nums[l] + nums[r]
            if suma == target:
                solutions +=  [[nums[l], nums[r]]]
                buf = nums[l]
                while l < r and nums[l] == buf:
                    l += 1
                buf = nums[r]
                while l < r and nums[r] == buf:
                    r -= 1
                
            elif suma < target:
                l += 1
            else:
                r -= 1
        return solutions

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)

        if len(nums) < 3:
            return []
        
        solutions = []

        for i in range(len(nums)-2):
            n = nums[i]
            if i == 0 or n != nums[i-1]:
                # unique
                ans = self.twoSum(nums[i+1:], -n)
                for sol in ans:
                    solutions.append([n, sol[0], sol[1]])

        return solutions
