class Solution:
    def countSubstrings(self, s: str) -> int:
        totalPalindromes = 0
        for i in range(len(s)):
            if(i > 0):
                l,r = i-1,i
                isPalindrome = True
                while(l >= 0 and r < len(s)):
                    if(s[l] != s[r]):
                        isPalindrome = False
                        break
                    else:
                        totalPalindromes +=1
                        l-=1
                        r+=1
            l,r = i,i
            isPalindrome = True
            while(l >= 0 and r < len(s)):
                if(s[l] != s[r]):
                    isPalindrome = False
                    break
                else:
                    totalPalindromes +=1
                    l-=1
                    r+=1

        return totalPalindromes