class Solution(object):
    def addStrings(self, num1, num2):
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        ans = ""

        while i >= 0 or j >= 0:
            if i >= 0:
                a = ord(num1[i]) - ord('0')
            else:
                a = 0

            if j >= 0:
                b = ord(num2[j]) - ord('0')
            else:
                b = 0

            total = a + b + carry

            ans = str(total % 10) + ans
            carry = total // 10

            i -= 1
            j -= 1

        if carry:
            ans = str(carry) + ans

        return ans