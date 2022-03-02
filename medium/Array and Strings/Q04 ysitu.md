[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/)




Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```
Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
Example 3:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```
Example 4:
```
Input: s = ""
Output: 0
```

Constraints:
```
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
```
-----
# 思路
双指针法。移动靠前的指针，如果出现重复的，就把靠后的指针向前移动，直到没有重复为止，并且记录最新的字符串长度。

# Python
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return(0)
        prev = curr = 0
        thestr = ''
        strlen = 0
        while curr <= len(s) - 1:
            if s[curr] in thestr:
                prev += 1
                strlen = max(len(thestr), strlen)
                thestr = s[prev:curr]
            else:
                thestr = thestr + s[curr]
                curr += 1
            # print(thestr)
            # print(strlen)
        strlen = max(len(thestr), strlen)
        return(strlen)
```
Runtime: 85 ms          63%
Memory Usage: 14.1 MB   74%


