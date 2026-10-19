class Solution:
    def nextGreatestLetter(self, letters, target):
        for i in range(len(letters)):
            if letters[i] > target:
                return letters[i]

        return letters[0]