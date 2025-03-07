from typing import List

class Solution:
    def closestPrimes(self, debut: int, fin: int) -> List[int]:
        if fin < 2 or debut > fin: 
            return [-1, -1]
        
        limite = int(fin ** 0.5) + 1
        crible = [True] * (limite + 1)
        crible[0], crible[1] = False, False
        for i in range(2, limite):
            if crible[i]:
                for j in range(i * i, limite, i):
                    crible[j] = False
        petits_primes = [i for i in range(2, limite) if crible[i]]
        
        tableau = [True] * (fin - debut + 1)
        
        if debut == 1:
            tableau[0] = False
        
        for p in petits_primes:
            start = max(p * p, debut + (p - debut % p) % p)
            for j in range(start, fin + 1, p):
                tableau[j - debut] = False
        
        primes = [i for i in range(debut, fin + 1) if tableau[i - debut]]
        
        if len(primes) < 2:
            return [-1, -1]
        
        min_ecart = float('inf')
        resultat = [-1, -1]
        
        for i in range(1, len(primes)):
            ecart = primes[i] - primes[i - 1]
            if ecart < min_ecart:
                min_ecart = ecart
                resultat = [primes[i - 1], primes[i]]
        
        return resultat
