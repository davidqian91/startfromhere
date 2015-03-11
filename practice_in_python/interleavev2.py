##Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
##
##1.guess: the last character should be in either s1 or s2
# 2.subproblems: prefixes
# the prefixes of s3 should be interleaving of some prefixes of s1 and s2.
# 3.recurrence:
# def Dp[i,j,k] denotes that the s3[1...k] is interleaving of
# s1[1..i] and s2[1..j]
# since length of prefixes of s3 should always equal to length
# of prefixes of s1 and s2.
# def Dp[i][j] = whether prefixes s3[1...i+j] is
# interleaving of prefixes s1[1..i] and s2[1..j]
# Dp[0][0] =True, since "" is interleaving of "" and ""
# otherwise:
# Dp[i][j] = (Dp[i-1][j] and s1[i-1] == s3[i+j-1])
# or (Dp[i][j-1] and s2[j-1] == s3[i+j-1])


class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        Dp = [[False for col in range(len(s2)+1)] for row in range(len(s1)+1)]
        Dp[0][0] = True
        # work on array boundaries
        for i in range(1, len(s1) + 1, 1):
            Dp[i][0] = Dp[i-1][0] and (s1[i-1] == s3[i-1])
        for j in range(1, len(s2) + 1, 1):
            Dp[0][j] = Dp[0][j-1] and (s2[j-1] == s3[j-1])
        # i denotes the number of characters in
        # current prefixes of s3 is from s1
        for i in range(1, len(s1)+1, 1):
            # j denotes the number of characters in
            # current prefixes of s3 is from s2
            for j in range(1, len(s2)+1, 1):
                # prefixes of s3[1.. i+j] is interleaving
                # of prefixes s1[1..i] and s2[1..j]
                Dp[i][j] = (Dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (Dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return Dp[len(s1)][len(s2)]
