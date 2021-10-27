[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/)

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:
```
Input: nums = [1,2,3,1]
Output: true
```
Example 2:
```
Input: nums = [1,2,3,4]
Output: false
```
Example 3:
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 ```

Constraints:
```
1 <= nums.length <= 105
-109 <= nums[i] <= 109
```

-----
# 解法
利用集合(set())能够去除重复项的特性
## Python3
```python3
    if len(set(nums)) < len(nums):
        return(True)
    else:
        return(False)
        
Runtime: 116 ms
Memory Usage: 20.2 MB
```