[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/)

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:
```
Input: s = "leetcode"
Output: 0
```
Example 2:
```
Input: s = "loveleetcode"
Output: 2
```
Example 3:
```
Input: s = "aabb"
Output: -1
 ```

Constraints:
```
1 <= s.length <= 105
s consists of only lowercase English letters.
```

-----
# 解法
我感觉比较节省循环次数的方法应该是取集合，然后针对集合里面每一个元素来计算其出现次数。      
但是尝试了一会发现集合这个排序的问题要单独解决比较费时间。     
最后就用了笨办法，针对每个元素进行全局搜索，直到遇到一个只出现一次的元素为止。    

——看了其他人的解法之后发现和我的解法1逻辑一样！但是速度快很多！奇怪……
倒是从他们的办法里想到了用集合能够提速的方法——把所有只出现一次的元素index保存，返回最小的就可以。。。

# Python3
解法1
```python3
class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        for i in range(n):
            if s.count(s[i]) == 1:
                return(i)
        return(-1)

Runtime: 4936 ms
Memory Usage: 14.5 MB   (45.24%)
```
解法2
```python3
class Solution:
    def firstUniqChar(self, s: str) -> int:
        sset = set(s)
        candidates = []
        for item in sset:
            if s.count(item) == 1:
                candidates.append(s.find(item))
        if len(candidates) > 0:
            return(min(candidates))
        else:
            return(-1)

Runtime: 48 ms          (99.33%)
Memory Usage: 14.6 MB   (21.24%)
```