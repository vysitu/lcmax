[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/)


Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:
```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```
Example 2:
```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 ```

Constraints:
```
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 ```

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

----- 
# 解法
- 题目要求modify the list in-situ
- do not need to return any value
## 方法1
- 剪断，然后把左边的append到右边的后面
- 利用index可以为负数的特性
## 方法2
- 新开一个列表，然后按照顺序把内容写进去

# Python3
## Solution 1
```python3
nums = nums[-1*k:][:]+nums[:-1*k][:]
## solution 1 simplified
nums = nums[-k:]+nums[:-k]
```
## Solution 2
```python3
    t1 = [0]*len(nums)
    for i in range(len(nums)):
        if i+k <len(nums):
            t1[i+k] = nums[i]
        else:
            t1[i+k-len(nums)] = nums[i]
    nums = t1.copy()
```
