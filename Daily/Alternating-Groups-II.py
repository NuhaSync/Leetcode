from typing import List

class Solution:
    def numberOfAlternatingGroups(self, couleurs: List[int], k: int) -> int:
        n = len(couleurs)
        resultat = 0
        gauche = 0
        droite = 1

        while droite < n + k - 1:
            if couleurs[droite % n] == couleurs[(droite - 1) % n]:
                gauche = droite
                droite += 1
                continue

            droite += 1

            if droite - gauche < k:
                continue

            resultat += 1
            gauche += 1

        return resultat
