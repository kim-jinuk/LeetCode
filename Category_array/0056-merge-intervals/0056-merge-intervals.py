class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if answer and i[0] <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1], i[1])
            else:
                answer.append(i)
        
        return answer