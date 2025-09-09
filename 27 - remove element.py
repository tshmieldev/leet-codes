class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
977
        c = 0

        for num in nums:
            if num != val:
                nums[c] = num
                c += 1
        
        return c