[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/)




Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```
Example 2:
```
Input: nums = []
Output: []
```
Example 3:
```
Input: nums = [0]
Output: []
 ```

Constraints:
```
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
```

-----
# 解法
抄的网友的解法。这个方法和我以为的什么hash的方法看上去差别还挺大的，我认为是因为题目要求总和为0的缘故。

首先排序，然后循环一个指向中间那个数的指针。指针左边取一个值，右边取一个值相加，得到总和s，然后这个s必须是0。和之前的两个数字相加比，其实并没有复杂很多，所以效率依然比较高。

# Python3
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1  # r is the last one
            while l < r:
                s3 = nums[l] + nums[i] + nums[r]
                if s3 > 0:
                    r -= 1
                elif s3 < 0:
                    l += 1
                else:
                    result.append([nums[l], nums[i], nums[r]])
                    while (l < r) and (nums[l] == nums[l+1]):
                        l += 1
                    while (l < r) and (nums[r] == nums[r-1]):
                        r -= 1
                    l += 1
                    r -= 1
        return(result)

```