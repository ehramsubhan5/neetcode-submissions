class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        rounds = 0
        while l <= r:
            kPossible = l + ((r - l) // 2)
            rounds = 0
            for p in piles:
                rounds += math.ceil(p / kPossible)
            if rounds > h:
                l = kPossible + 1
            else:
                k = min(k, kPossible)
                r = kPossible - 1
        return k