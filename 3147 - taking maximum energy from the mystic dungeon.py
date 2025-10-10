class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        for x in range(1, ceil(n/k)):
            for s in range(k):
                idx = x*k + s

                if idx >= n:
                    continue
                
                if idx >= k:
    
                    energy[idx] = max(energy[idx], energy[idx] + energy[idx-k])
                  
        best = max(energy[-k:])
        return best