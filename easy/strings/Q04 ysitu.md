[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/)


Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:
```
Input: s = "anagram", t = "nagaram"
Output: true
```
Example 2:
```
Input: s = "rat", t = "car"
Output: false
 ```

Constraints:
```
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 ```

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

-----
# 解法
转换成列表，然后排序，如果排序后的两个列表完全一样，那么就是anagram，否则就不是。

# Python3
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = []
        l2 = []
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return(False)
        else:
            for i in range(n1):
                l1.append(s[i])
                l2.append(t[i])
        l1.sort()
        l2.sort()
        return(l1 == l2)

Runtime: 56 ms          (47.38%)
Memory Usage: 15.4 MB


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return(False)
        l1 = list(s)
        l2 = list(t)
        l1.sort()
        l2.sort()
        return(l1 == l2)

Runtime: 48 ms          (73.26%)
Memory Usage: 15.1 MB   (9.47%)
```

# 网友的方法
是计数法
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elif set(s) != set(t):
            return False
        else:
            for i in set(s):
                if s.count(i) != t.count(i):
                    return False
            return True
```