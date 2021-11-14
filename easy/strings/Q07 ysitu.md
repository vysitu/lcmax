[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/)



Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:
```
Input: haystack = "hello", needle = "ll"
Output: 2
```
Example 2:
```
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```
Example 3:
```
Input: haystack = "", needle = ""
Output: 0
 ```

Constraints:
```
0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
```


-----
# 解法
暴力解决……

# Python3
```python3
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (len(needle) == 0):
            return(0)
        elif (len(haystack) < len(needle)):
            return(-1)
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                return(-1)
            if haystack[i:i+len(needle)] == needle:
                return(i)
        return(-1)
    
Runtime: 56 ms          (61.55%)
Memory Usage: 14.4 MB   (44.94%)
```