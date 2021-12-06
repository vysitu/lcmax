[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/801/)




A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

 

Example 1:
```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```
Example 2:
```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 ```

Constraints:
```
1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
```

-----
# 解法
乍一看挺简单的，这个是一个非常“数学”的题目，既然是求峰值，那么导数就是从正变成负。
但是对于这个离散的东西（列表）而言并不需要那么复杂，只要知道一个元素比左右两边元素大就行。采用滑动窗口的方法，一路做判断即可。

做了之后发现在没有峰值的时候返回最大值的index，这一点挺坑的。

还有就是要在O(logN)的时间复杂度下完成，这个难度一下就上去了。用滑动的办法的话，最糟糕的情况就是O(N)。我看了其他人的解答，主要都是用的二分法的思路，那样确实可以省一些时间，但是在特定情况下并不比滑动的办法更快，比如构造成一连串正弦曲线那样的，就可能要找到最后一组才找到，滑动的话一开始就找到了……

想了一下之后，在二分法的基础上还可以搞出一种蠕动法，蠕动法就是一路顺着坡度往上爬，爬到顶为止，反正找到一个peak就够了。我觉得这种方法其实更好，特别对于噪声较大的数据而言。


# Python3
```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return(0)
        for idx in range(1, len(nums)-1):
            if (nums[idx]>nums[idx-1]) and (nums[idx]>nums[idx+1]):
                return(idx)
        return(nums.index(max(nums)))

# 蠕动法
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        p = int(len(nums)/2)
        while True:
            if (p == len(nums)-1) or (p==0):
                return(nums.index(max(nums)))
            if (nums[p] > nums[p-1]) and (nums[p] > nums[p+1]):
                return(p)
            elif nums[p+1] > nums[p-1]:
                p += 1
            else:
                p-=1
```