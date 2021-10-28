[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/)

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:
```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```
Example 2:
```
Input: nums = [0]
Output: [0]
 ```

Constraints:
```
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 ```

Follow up: Could you minimize the total number of operations done?

-----
# 解法
可以用双指针，和Q1相似的思路，一个指向当前元素，一个指向0的位置。这方法会打乱输出顺序，不使用。
还可以直接把所有0数出来然后添加到最后。

# Python3
```python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        for n in range(zeros):
            nums.remove(0)
            nums.append(0)

Runtime: 592 ms             (10%)
Memory Usage: 15.5 MB       (28%)
```

-----
速度最快的那一批，思路和我那个交换元素的方法差不多
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) == 0:
            return
        
        j = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
                else:
                    j += 1
            
        return
