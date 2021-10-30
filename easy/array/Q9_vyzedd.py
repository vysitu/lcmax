
#Dumb solution time complexity O(n * n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leftPointer = 0
        rightPointer = 1
        
        while leftPointer != len(nums):
            for j in range(rightPointer, len(nums)):
                
                if nums[leftPointer] + nums[j] == target:
                    return[leftPointer, j]
                
            leftPointer += 1
            rightPointer += 1
            

#Smarter solution -> time complexity O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        
        for x, ele in enumerate(nums):
            
            n = target - ele
            
            if n not in dic:
                dic[ele] = x
                
            else:
                return [dic[n], x]
            
