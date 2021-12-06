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

-----
# 解法
本来做完Q02就可以了，手贱点进来，发现这题直接用sort不就能搞定了……
可能其他语言要从头实现一个排序吧。

# Python3
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return(nums[::-1][k-1])
```