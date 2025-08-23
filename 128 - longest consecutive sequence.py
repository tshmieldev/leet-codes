class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        numset = set(nums)
        length = 0
        longest = 1
        for num in numset:
            if num-1 not in numset:
                # start of a seq
                length = 1
                while num + length in numset:
                    length += 1
                    longest = max(longest,length)
            
        return longest
