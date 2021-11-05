#My stupid solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            
            try:
            
                if i == 0:
                    nums.pop(nums.index(0))
                    nums.append(0)
                    
            except:
                
                IndexError
        
        return nums

#Smarter solution (Two Pointer)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                
        
