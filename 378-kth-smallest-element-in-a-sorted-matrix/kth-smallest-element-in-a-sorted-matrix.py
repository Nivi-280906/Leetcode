class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)

        low = matrix[0][0]
        high = matrix[n - 1][n - 1]

        while low < high:
            mid = (low + high) // 2

            count = 0

            # Count elements <= mid
            for row in matrix:
                left = 0
                right = n

                while left < right:
                    m = (left + right) // 2

                    if row[m] <= mid:
                        left = m + 1
                    else:
                        right = m

                count += left

            if count < k:
                low = mid + 1
            else:
                high = mid

        return low