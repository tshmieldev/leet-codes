class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        drank = 0
        while empty >= numExchange or numBottles:
            drank += numBottles
            empty += numBottles
            numBottles = 0
            if empty >= numExchange:
                empty -= numExchange
                numExchange += 1
                numBottles += 1
        return drank