class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) -1

        while l <= r:

            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            if nums[l] > nums[m]:
                # rotation in the left side
                # searched value may be here

                if nums[m] < target and nums[r] >= target:
                    # but it's not, it's in the right partition.
                    l = m + 1
                else:
                    # it is indeed in here.
                    r = m - 1

            elif nums[m] > nums[r]:
                # rotation in the right side
                # searched value may be here

                if nums[m] > target and nums[l] <= target:
                    # but it's not, it's in the left partition.
                    r = m - 1
                else:
                    # it is indeed in here.
                    l = m + 1
            else:
                # clean partition.
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
        return -1