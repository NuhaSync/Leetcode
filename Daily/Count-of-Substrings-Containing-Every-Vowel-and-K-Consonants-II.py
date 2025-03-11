class Solution:
    def countOfSubstrings(self, mot: str, k: int) -> int:
        voyelles = {'a', 'e', 'i', 'o', 'u'}
        compteur_voyelles = {}
        compteur_consonnes, gauche, sub_strings = 0, 0, 0
        prochaine_consonne = [0] * len(mot)
        prochaine_index = len(mot)

        for i in range(len(mot) - 1, -1, -1):
            prochaine_consonne[i] = prochaine_index
            if mot[i] not in voyelles:
                prochaine_index = i

        for droite in range(len(mot)):
            caractere = mot[droite]

            if caractere in voyelles:
                compteur_voyelles[caractere] = compteur_voyelles.get(caractere, 0) + 1
            else:
                compteur_consonnes += 1

            while compteur_consonnes > k:
                premier_caractere = mot[gauche]
                if premier_caractere in voyelles:
                    compteur_voyelles[premier_caractere] -= 1
                    if compteur_voyelles[premier_caractere] == 0:
                        del compteur_voyelles[premier_caractere]
                else:
                    compteur_consonnes -= 1
                gauche += 1

            while gauche < len(mot) and len(compteur_voyelles) == 5 and compteur_consonnes == k:
                sub_strings += prochaine_consonne[droite] - droite
                premier_caractere = mot[gauche]
                if premier_caractere in voyelles:
                    compteur_voyelles[premier_caractere] -= 1
                    if compteur_voyelles[premier_caractere] == 0:
                        del compteur_voyelles[premier_caractere]
                else:
                    compteur_consonnes -= 1
                gauche += 1

        return sub_strings
