class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        substring = {}
        permutation = {}
        for r in range (len(s1)):
            permutation[s1[r]] = 1 + permutation.get(s1[r], 0)
    
        for r in range(len(s2)):
            substring[s2[r]] = 1 + substring.get(s2[r], 0)

            if r - l > len(s1) - 1:
                charleft = s2[l]
                substring[charleft] -= 1
                if substring[charleft] == 0:
                    del substring[charleft]
                l += 1
            if len(substring) == len(permutation) and substring == permutation:
                return True
        return False