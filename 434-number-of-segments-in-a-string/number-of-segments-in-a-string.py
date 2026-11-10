
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        return len(words)
