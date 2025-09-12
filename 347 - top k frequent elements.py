class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return map(lambda a: a[0], sorted(Counter(nums).items(), key=lambda i: i[1], reverse=True)[:k])