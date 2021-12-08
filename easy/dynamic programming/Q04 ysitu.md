[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/)


You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```
Example 2:
```
Input: nums = [2,7,9,3,1]

Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 ```

Constraints:
```
1 <= nums.length <= 100
0 <= nums[i] <= 400
```

-----
# 解法
[网友答案及解析](https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/discuss/55696/Python-solution-3-lines.)

说实话，这个题的解法我不是特别确定。网友答案看上去并不像是能做出来的样子，但是就是可以做出来。

逻辑倒是很简单。这个题目乍一看就是1级-2级楼梯的问题，不过强制要跳过一级楼梯，所以具体实现起来就不能照搬，更像是2级和3级楼梯之间选。

# Python3
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return(max(nums))
        else:
            prev = curr = 0
            for num in nums:
                prev, curr = curr, max(prev + num, curr)
        return(curr)
```