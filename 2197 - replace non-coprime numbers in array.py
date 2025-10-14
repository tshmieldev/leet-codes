import math
class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        start = 0
        while True:
            c = start
            for i in range(start, len(nums)-1):
                if i > 4:
                    start = i - 4
                if math.gcd(nums[i], nums[i+1]) > 1:
                    nums = nums[:i] + [math.lcm(nums[i], nums[i+1])] + nums[i+2:]
                    break
                c += 1
            if c == len(nums) - 1:
                break
        
        return nums

def printfirstfive(a):
    print(a[:5])