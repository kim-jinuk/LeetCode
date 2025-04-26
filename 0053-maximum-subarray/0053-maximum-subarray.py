class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        arr = [nums[0]]
        for i in range(1, len(nums)):
            arr.append(max(nums[i], nums[i] + arr[i - 1]))
        
        return max(arr)