class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        l=len(candyType)
        n=len(set(candyType))
        return min(n,l//2)
        