class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        s = 0 
        for x, y in c.items():
            if y == max(c.values()):
                s += y
        return s