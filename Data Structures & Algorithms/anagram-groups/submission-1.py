class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            sortedi = ''.join(sorted(i))
            res[sortedi].append(i)
        return list(res.values())
