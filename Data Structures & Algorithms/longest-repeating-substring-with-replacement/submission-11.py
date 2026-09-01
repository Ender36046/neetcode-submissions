class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        hashmap = {}
        longest = 0
        while r < len(s):
            hashmap[s[r]] = hashmap.get(s[r],0)+1
            if(r-l -max(hashmap.values()) +1 > k):
                hashmap[s[l]] -=1
                l+=1
            r +=1
            longest = max(longest,r-l)
        return longest