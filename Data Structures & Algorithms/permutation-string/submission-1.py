class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap_s1, hashmap_s2 = {}, {}
        for i in s1:
            hashmap_s1[i] = hashmap_s1.get(i, 0)+1
        print(hashmap_s1)
        l,r = 0,0

        while r < len(s2):
            hashmap_s2[s2[r]] = hashmap_s2.get(s2[r], 0)+1
            print(hashmap_s2)
            while(r-l +1 > len(s1)):
                hashmap_s2[s2[l]] -=1
                if hashmap_s2[s2[l]] == 0: hashmap_s2.pop(s2[l])
                l+=1
            if(hashmap_s1 == hashmap_s2):
                return True
            r+=1
        
        return False
