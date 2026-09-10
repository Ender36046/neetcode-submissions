"""

2D array to represent DP

use arr[j][i] = max(arr[j-1][i], arr[j][i-1]), 

then if str1[i] == str2[j] use arr[j-1][i-1]



"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        arr = [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if(text1[i-1] == text2[j-1]):
                    arr[j][i] = arr[j-1][i-1]+1
                else:
                    arr[j][i] = max(arr[j-1][i], arr[j][i-1])
        return arr[len(text2)][len(text1)]
        