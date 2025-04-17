class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        answer = []
        i = 0
        n = len(intervals)
        while (i <= n - 1):
            max_value = intervals[i][1]
            if (i == n - 1):
                answer.append([intervals[i][0], intervals[i][1]])
                return answer

            j = i + 1
            while (j < n and max_value >= intervals[j][0]):
                max_value = max(max_value, intervals[j][1])
                j += 1
            answer.append([intervals[i][0], max_value])
            i = j

        return answer