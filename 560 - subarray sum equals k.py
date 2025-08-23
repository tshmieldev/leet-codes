class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        sumMap = {
            0 : 1
        }

        count = 0
        suma = 0 
        for el in nums:
            suma += el

            if (suma - k) in sumMap:
                count += sumMap[suma-k]
            if suma in sumMap:
                sumMap[suma] += 1
            else:
                sumMap[suma] = 1
        return count
