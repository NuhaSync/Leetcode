class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dernier = [-1, -1, -1]
        total_sous_chaines = 0

        for i, char in enumerate(s):
            if char in "abc":
                dernier[ord(char) - ord('a')] = i

            if -1 not in dernier:
                total_sous_chaines += min(dernier) + 1

        return total_sous_chaines

