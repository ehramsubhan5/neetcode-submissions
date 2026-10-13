class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        #prefix values
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
            #this will iterate through and fill res
        #postfix values
        postfix = 1
        #start at the right side of res
        j = len(nums) - 1
        while j >= 0:
            res[j] *= postfix
            postfix *= nums[j]
            j -= 1
        return res