class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = nums[0]

        prev = (0, 0)
        cur = None
        for i in range(len(nums)):
            num = nums[i]
            
            if num == 0:
                prev = (0,0)
                mx = max(mx, 0)
                continue
            if num > 0:
                if prev == (0,0):
                    cur = (num, num)
                else:
                    cur = ((cur[0] or 1) * num, (cur[1] or 1) * num)
                mx = max(mx, cur[1])
            else:
                # negative
                if prev == (0,0):
                    cur = (num, 0)
                else:
                    cur = ((cur[0] or 1) * num, 0)
                    if cur[0] > 0:
                        cur = (cur[0], cur[0])
                        mx = max(mx, cur[1])  
            prev = cur
        return mx

S = Solution()
print(S.maxProduct([-1,0,-2]))
print(S.maxProduct([2,2,-1]))
print(S.maxProduct([-1,-2,-9,-6]))
print(S.maxProduct([2,-5,-2,-4,3]))