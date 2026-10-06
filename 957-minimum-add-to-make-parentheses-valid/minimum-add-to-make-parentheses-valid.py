class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        ans=0
        for i in s:
            if i=='(':
                count+=1
            else:
                if count>0:
                    count-=1
                else:
                    ans+=1
        return ans+count