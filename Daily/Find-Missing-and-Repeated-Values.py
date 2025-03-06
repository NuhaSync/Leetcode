class Solution:
    def findMissingAndRepeatedValues(self, grille: List[List[int]]) -> List[int]:
        nums = [num for ligne in grille for num in ligne]
        
        n = len(nums)
        somme_totale = sum(nums)
        somme_carrée_totale = sum(num * num for num in nums)
        
        somme_attendue = n * (n + 1) // 2
        somme_carrée_attendue = n * (n + 1) * (2 * n + 1) // 6
        
        diff_somme = somme_attendue - somme_totale
        diff_somme_carrée = somme_carrée_attendue - somme_carrée_totale
        
        manque = (diff_somme + (diff_somme_carrée // diff_somme)) // 2
        repete = manque - diff_somme
        
        return [repete, manque]
