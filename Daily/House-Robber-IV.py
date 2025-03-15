from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def peut_voler(cap):
            voles, i = 0, 0
            while i < len(nums):
                if nums[i] <= cap:
                    voles += 1
                    if voles == k:
                        return True
                    i += 1
                i += 1
            return False

        gauche, droite = min(nums), max(nums)
        while gauche < droite:
            milieu = (gauche + droite) >> 1
            if peut_voler(milieu):
                droite = milieu
            else:
                gauche = milieu + 1
        
        return gauche
