[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/)


Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

Example 1:
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```
Example 2:
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 ```

Constraints:
```
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
```

-----
# 解法
只保留字母，去掉空格，转成小写

# Python3
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        for i in range(len(s)):
            if s[i].isalnum():
                t += s[i].lower()
        nt = len(t)
        if nt <= 1:
            return(True)
        for p1 in range(nt):
            p2 = nt-p1-1
            if t[p1] != t[p2]:
                return(False)
            if p1>p2:
                return(True)

Runtime: 56 ms          (42.59%)
Memory Usage: 14.6 MB   (61.06%)
```