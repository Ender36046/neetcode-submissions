class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(len(t) > len(s)):
            return ""
        elif(t == s):
            return t
        l,r = 0,0

        hashmapT = {}
        hashmapWindow = {}

        res = ""
        resLen = float("infinity")

        for i in t:
            hashmapT[i] = hashmapT.get(i, 0) +1

        totalNeed = len(hashmapT)
        have = 0

        while(r < len(s)):
            ch = s[r]
            hashmapWindow[ch] = hashmapWindow.get(ch,0) +1
            if(ch in hashmapT and hashmapWindow[ch] == hashmapT[ch]):
                have +=1
            while(have == totalNeed):
                if(r-l +1) < resLen:
                    res = s[l:r+1] 
                    resLen = (r-l+1)

                hashmapWindow[s[l]] = hashmapWindow.get(s[l], 0) -1
                if s[l] in hashmapT and hashmapWindow[s[l]] < hashmapT[s[l]]:
                    have -=1

                l+=1
            r+=1
        return res