class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"

        # Negative sign
        sign = ""
        if (numerator < 0) != (denominator < 0):
            sign = "-"

        numerator = abs(numerator)
        denominator = abs(denominator)

        # Integer part
        integer = numerator // denominator
        remainder = numerator % denominator

        if remainder == 0:
            return sign + str(integer)

        ans = sign + str(integer) + "."

        # Store remainder and its position
        seen = {}

        while remainder != 0:
            if remainder in seen:
                pos = seen[remainder]
                ans = ans[:pos] + "(" + ans[pos:] + ")"
                return ans

            seen[remainder] = len(ans)

            remainder = remainder * 10
            digit = remainder // denominator
            ans += str(digit)

            remainder = remainder % denominator

        return ans