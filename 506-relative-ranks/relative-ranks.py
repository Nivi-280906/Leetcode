class Solution(object):
    def findRelativeRanks(self, score):
        
        sorted_score = score[:]
        sorted_score.sort(reverse=True)
        
        answer = []
        
        for s in score:
            position = sorted_score.index(s)
            
            if position == 0:
                answer.append("Gold Medal")
            elif position == 1:
                answer.append("Silver Medal")
            elif position == 2:
                answer.append("Bronze Medal")
            else:
                answer.append(str(position + 1))
        
        return answer