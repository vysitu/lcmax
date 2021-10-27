[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/)

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:
```
Input: nums = [2,2,1]
Output: 1
```
Example 2:
```
Input: nums = [4,1,2,1,2]
Output: 4
```
Example 3:
```
Input: nums = [1]
Output: 1
 ```

Constraints:
```
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
```

-----
# 解法
先进行排序，然后再利用相邻数值必然相同的特点，隔一个元素查一次，线性的顺着列表查下去。一旦出现相邻元素不一样的，那就必然是有问题的

## Python3
```python3
    nums.sort()
    for i in range(0,len(nums),2):  # sorted list, same values should be next to each other
        if i+1 ==len(nums):  # already the last element, must be the single one
            return(nums[i])
        if nums[i+1] != nums[i]: #the next element is not the same
            return(nums[i])

Runtime: 132 ms         (78.07%)
Memory Usage: 16.6 MB   (86.00%)
```