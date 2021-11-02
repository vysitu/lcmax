class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum_set = sum(set(nums))
        sum_list = sum(nums)
        res = 2 * sum_set - sum_list
        return res
