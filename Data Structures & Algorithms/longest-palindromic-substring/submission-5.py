class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestP = ""
        longestPLength = 0
        if(len(s) <= 1):
            return s

        for i in range(len(s)):
            #even case
            if(i > 0):
                isPalindrome = True
                newL = i-1
                newR = i
                while(newL >= 0 and newR < len(s)):
                    if(s[newL] != s[newR]):
                        isPalindrome = False
                        break
                    else:
                        if(isPalindrome and newR-newL >= longestPLength):
                            longestPLength = newR-newL
                            longestP = s[newL:newR+1]
                        newL -=1
                        newR +=1

            newL, newR = i,i
            isPalindrome = True
            while(newL >= 0 and newR < len(s)):
                if(s[newL] != s[newR]):
                    isPalindrome = False
                    break
                else:
                    if(isPalindrome and newR-newL >= longestPLength):
                        longestPLength = newR-newL
                        longestP = s[newL:newR+1]
                    newL -=1
                    newR +=1
        return longestP          