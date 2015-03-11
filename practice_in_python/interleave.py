##Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.


class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if not s3:
            if s1 or s2:
                return False
            else:
                return True
        if not s1 and not s2:
            return False
        elif not s1:
            if s2[0] != s3[0]:
                return False
            else:
                return self.isInterleave(s1, s2[1:], s3[1:])
        elif not s2:
            if s1[0] != s3[0]:
                return False
            else:
                return self.isInterleave(s1[1:], s2, s3[1:])
        else:
            if s1[0] != s3[0] and s2[0] != s3[0]:
                return False
            elif s1[0] != s3[0]:
                return self.isInterleave(s1, s2[1:], s3[1:])
            elif s2[0] != s3[0]:
                return self.isInterleave(s1[1:], s2, s3[1:])
            else:
                return self.isInterleave(s1, s2[1:], s3[1:]) or self.isInterleave(s1[1:], s2, s3[1:])
