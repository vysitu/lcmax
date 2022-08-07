[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/824/)




Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:
```
Input: nums = [3,2,3]
Output: 3
```
Example 2:
```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 ```

Constraints:
```
n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
 ```

Follow-up: Could you solve the problem in linear time and in O(1) space?

-----
# 解法
注意到，一个元素出现多于n/2次的话，这个元素在排序之后的列表里面是一定经过列表中点的。

排序并取中点的值之后，分析两种情况：
- 如果是偶数长度的列表，长度2n，那么majority元素至少有n+1个。Python从0开始计算列表元素的索引，所以n其实就是指向的第n+1个元素，这个点是那个元素必然经过的。
- 如果是奇数长度的列表，长度2n+1，那么majority元素至少有n+1个。len(List)/2得到的是n，这也是指向第n+1个元素的。

# Python3
```python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return(nums[int(len(nums)/2)])

```