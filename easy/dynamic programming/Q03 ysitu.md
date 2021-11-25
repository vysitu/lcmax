[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/)




Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```
Example 2:
```
Input: nums = [1]
Output: 1
```
Example 3:
```
Input: nums = [5,4,-1,7,8]
Output: 23
 ```

Constraints:
```
1 <= nums.length <= 105
-104 <= nums[i] <= 104
 ```

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

-----
# 解法
有空可以探讨一下这个。
我没有什么概念，这个题是看的其他人的答案。
这个答案里面用的方法是：
    新加的值和当前累积的和对比，
        如果更大就替换当前值；
        如果没有继续变大（接下来的元素是负数），保留之前的最大值；
    总的累积的和和当前累积的对比，初始值是0
        如果当前累积的变得小于0（负数太多），那么保留之前最大的；
        如果接下来的一段比之前的更大，保留接下来一段里面最大的。

```python3
class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

```