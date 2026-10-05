class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #hashmap
        #An array with empty arrays about the size of our nums + 1
        freq = [[] for i in range(len(nums) + 1)]
        #go through every value in nums and count how many times they occur
        for n in nums:
            # 1 + current count and if it doesn't exist in map yet, default value 0
            count[n] = 1 + count.get(n, 0)
        #going through each value we counted; count.items returns every key:value pair
        for n, c in count.items():
            #this value of n occurs exactly c number of times
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res