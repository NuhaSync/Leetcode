class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        compteur_blanc = sum(1 for i in range(k) if blocks[i] == 'W')
        min_ops = compteur_blanc

        for i in range(k, n):
            if blocks[i - k] == 'W':
                compteur_blanc -= 1
            if blocks[i] == 'W':
                compteur_blanc += 1
            min_ops = min(min_ops, compteur_blanc)

        return min_ops