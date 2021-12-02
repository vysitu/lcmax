[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/798/)




Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:
```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```
Example 2:
```
Input: nums = [2,0,1]
Output: [0,1,2]
```
Example 3:
```
Input: nums = [0]
Output: [0]
```
Example 4:
```
Input: nums = [1]
Output: [1]
 ```

Constraints:
```
n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.
 ```

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

-----
# 解法
in-place操作，对于这种只有3种类型的列表很简单，只要一种往前移，一种往后移，剩下一种原地不动就行。

# Python3
```python3
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) ==1:
            return(nums)
        ind = 0
        opcount = 0
        while True:
            x = nums.pop(ind)
            if x == 0:
                nums.insert(0,x)
                ind += 1
            elif x == 2:
                nums.append(x)  # 原来的元素移到末尾了，所以本index指向的已经是下一个元素了
            else:
                nums.insert(ind, x)
                ind += 1
            if ind == len(nums):
                break
            opcount += 1 
            if opcount > len(nums):   #防止最后在一串2上面不停的循环
                break
        return(nums)

Runtime: 28 ms          (92.04%)
Memory Usage: 14.3 MB


# 还有一招比较血腥的办法，也只遍历一次，然后直接用新数组覆盖原来的。
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        count1 = 0
        count2 = 0
        for x in nums:
            if x == 0:
                count0 += 1
            elif x == 1:
                count1 += 1
            else:
                count2 += 1
        nums[:] = count0*[0]+count1*[1]+count2*[2]
        return(nums)

Runtime: 32 ms          (76.58%)
Memory Usage: 14.2 MB   (75.88%)
```