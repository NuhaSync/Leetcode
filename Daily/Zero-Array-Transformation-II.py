from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], reqs: List[List[int]]) -> int:
        n = len(nums)
        s, k = 0, 0
        delta = [0] * (n + 1)
        
        for i in range(n):
            while s + delta[i] < nums[i]:
                k += 1
                if k > len(reqs):
                    return -1
                g, d, v = reqs[k - 1]
                if d >= i:
                    delta[max(g, i)] += v
                    delta[d + 1] -= v
            s += delta[i]
        
        return k
