from typing import List

class Solution:
    def maximumCandies(self, bonbons: List[int], enfants: int) -> int:
        total = sum(bonbons)
        if total < enfants:
            return 0
        
        gauche, droite = 1, total // enfants
        while gauche < droite:
            milieu = (gauche + droite + 1) // 2
            if sum(b // milieu for b in bonbons) >= enfants:
                gauche = milieu
            else:
                droite = milieu - 1
        
        return gauche
