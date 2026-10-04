class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         hashset = set()
         for n in nums:
            if n in hashset:
                return True
            hashset.add(n) #add n to hashset every iteration
         return False