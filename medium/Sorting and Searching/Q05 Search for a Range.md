[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/802/)




Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```
Example 2:
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```
Example 3:
```
Input: nums = [], target = 0
Output: [-1,-1]
 ```

Constraints:
```
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
```

-----
# 解法
这个题目就差把“二分法”三个字写脸上了！
直接用二分法找到任何一个元素，然后开始朝两个方向查找就可以了。

但是我就不，嘿嘿

我觉得作为搞算法和数据的，很关键的一个立场就是，有现成的工具就要用，特别是这工具已经优化到相当程度的情况下。

# Python3
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            left = nums.index(target)
            right = (len(nums) - 1) - nums[::-1].index(target)
            return([left,right])
        except:
            return([-1,-1])

Runtime: 76 ms          (97.4%)
Memory Usage: 15.5 MB   (54.6%)
```