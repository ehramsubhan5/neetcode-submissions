class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashset
        hashset = set()

        #iterate thru nums
        for i in nums:
            #check hashset
            if i in hashset:
                return True
            hashset.add(i)
        return False