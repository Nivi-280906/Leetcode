
class Solution(object):
    def deserialize(self, s):
        
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ""

        for ch in s:

            if ch == '[':
                stack.append(NestedInteger())

            elif ch == '-' or ch.isdigit():
                num += ch

            elif ch == ',' or ch == ']':
                
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""

                if ch == ']':
                    if len(stack) > 1:
                        temp = stack.pop()
                        stack[-1].add(temp)

        return stack[0]
