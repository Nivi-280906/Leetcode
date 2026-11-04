class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        ugly = [1] * n
        index = [0] * len(primes)

        for i in range(1, n):
            mini = float('inf')

            for j in range(len(primes)):
                value = primes[j] * ugly[index[j]]
                mini = min(mini, value)

            ugly[i] = mini

            for j in range(len(primes)):
                if primes[j] * ugly[index[j]] == mini:
                    index[j] += 1

        return ugly[n - 1]