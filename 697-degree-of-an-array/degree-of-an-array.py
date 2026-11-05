class Solution(object):
    def findShortestSubArray(self, nums):
        count = {}
        first = {}
        last = {}

        for i in range(len(nums)):
            num = nums[i]

            if num not in count:
                count[num] = 0
                first[num] = i

            count[num] += 1
            last[num] = i

        degree = max(count.values())
        mini = len(nums)

        for num in count:
            if count[num] == degree:
                length = last[num] - first[num] + 1
                mini = min(mini, length)

        return mini