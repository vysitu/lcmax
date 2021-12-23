[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/800/)




Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```
Example 2:
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 ```

Constraints:
```
1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
```

Solutions:
```
不明白考点是什么，题目也没说不能使用内建函数
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
Runtime: 56 ms
Memory Usage: 15.2 MB
```