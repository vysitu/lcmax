#Dumb solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        while count != k:
            temp = nums[-1]
            nums.insert(0, temp)
            nums.pop(-1)
            count += 1
        
        return nums

#Smarter solution

