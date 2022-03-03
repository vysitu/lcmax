[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/)





Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.


Example 1:
```
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
```
Example 2:
```
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
```
Example 3:
```
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 ```

Constraints:
```
1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 ```

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

-----
# 解法
我觉得我大概知道方法，然而并不知道。看了答案之后还是有点不清楚。

# Python
```
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return(False)
        p1 = max(nums)
        p2 = max(nums)
        ans = False
        for i in range(len(nums)):
            if p1 > nums[i]:
                p1 = nums[i]
            elif (p1 < nums[i]) and (p2 > nums[i]):
                p2 = nums[i]
            if (nums[i] > p1) and (nums[i] > p2):
                ans = True
                break
        return(ans)

Runtime: 838 ms         45%
Memory Usage: 24.7 MB   71%
```