[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/)

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:
```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```
Example 2:
```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Explanation: [9,4] is also accepted.
 ```

Constraints:
```
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 ```

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


-----
# 解法
利用集合能够去重复的特性，然后利用List.count来计算元素数量，最后构造新的列表。

# Python3
```python3
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i1 = set(nums1).intersection(set(nums2))
        output = []
        for item in i1:
            k = min(nums1.count(item), nums2.count(item))
            output = output+ [item]*k
        return(output)

Runtime: 68 ms              (36%)
Memory Usage: 14.6 MB       (70%)
```

-----
也有用字典来解的
```python3
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = {}
        res = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1

        return res
```