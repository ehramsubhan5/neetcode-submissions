class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        #Create hashmaps
        for i in range(len(s)):
            #change value of key (s[i])
            countS[s[i]] = 1 + countS.get(s[i], 0) #sets default value for key in case it does not exist in hashmap
            countT[t[i]] = 1 + countT.get(t[i], 0)

        #check that each key value is equal
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
