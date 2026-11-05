class Solution(object):
    def findLengthOfLCIS(self, nums):
        count = 1
        maxi = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                count = 1

            maxi = max(maxi, count)

        return maxi