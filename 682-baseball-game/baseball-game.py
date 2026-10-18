class Solution(object):
    def calPoints(self, operations):
        record = []

        for x in operations:
            if x == "C":
                record.pop()

            elif x == "D":
                record.append(record[-1] * 2)

            elif x == "+":
                record.append(record[-1] + record[-2])

            else:
                record.append(int(x))

        return sum(record)