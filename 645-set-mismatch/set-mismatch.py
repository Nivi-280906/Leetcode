class Solution(object):
    def findErrorNums(self, nums):
        seen = set()
        duplicate = 0

        for i in nums:
            if i in seen:
                duplicate = i
            seen.add(i)

        missing = 0

        for i in range(1, len(nums) + 1):
            if i not in seen:
                missing = i

        return [duplicate, missing]