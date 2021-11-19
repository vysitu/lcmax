class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums) + 1
        
        return sum(range(N)) - sum(nums)
