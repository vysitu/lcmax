[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/)




Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```
Example 2:
```
Input: nums = [1], k = 1
Output: [1]
 ```

Constraints:
```
1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 ```

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

-----
# 解法
这个题需要多刷。我目前用的方法效率很低。
我觉得我用的理念是可以的，就是直接拉高维度，把1D列表变成2D列表，这样每个列表里面的元素都一样，操作起来更方便。
但是python不import的话并没有什么好办法返回前N个值的index，所以我这个方法效率依然很低。
在这种情况下用字典效率也很低，因为字典只适合用key查value，而不能反过来根据value查key。

应该是由于同样的原因，使用带两个元素的列表速度也很慢。可以用sorted+lambda来得到里面某个元素的出现频率，这一点还是很好的。学到了一个新招数。

# Python3
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        uniq = list(set(nums))
        d2 = []
        for item in uniq:
            d2.append([])
        for item in nums:
            d2[uniq.index(item)].append(item)
        d2len = []
        for i in d2:
            d2len.append(len(i))
        output = []
        for i in range(k):
            temp = d2.pop(d2len.index(max(d2len)))
            temp2 = d2len.pop(d2len.index(max(d2len)))
            output.append(temp[0])
        return(output)

# 使用带两个元素的列表，一个记录值，一个记录出现次数，用sorted+lambda来得到其中某个元素的出现频率。
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        uniq = list(set(nums))
        uniq.sort()
        output = [[0,i] for i in uniq]
        for item in nums:
            idx = uniq.index(item)
            output[idx][0] += 1
        output = sorted(output, key = lambda x:x[0]
                        , reverse = True)
        actual = [i[1] for i in output[:k]]
        return(actual)
```