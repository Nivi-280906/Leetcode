class Solution:
    def maximumGap(self, nums):
        n = len(nums)

        if n < 2:
            return 0

        mn = min(nums)
        mx = max(nums)

        if mn == mx:
            return 0

        gap = (mx - mn + n - 2) // (n - 1)

        bucket_min = [float('inf')] * n
        bucket_max = [float('-inf')] * n

        for x in nums:
            index = (x - mn) // gap

            bucket_min[index] = min(bucket_min[index], x)
            bucket_max[index] = max(bucket_max[index], x)

        ans = 0
        previous = mn

        for i in range(n):
            if bucket_max[i] == float('-inf'):
                continue

            ans = max(ans, bucket_min[i] - previous)
            previous = bucket_max[i]

        return ans