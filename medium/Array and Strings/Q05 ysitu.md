[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/)




Given a string s, return the longest palindromic substring in s.

 

Example 1:
```
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```
Example 2:
```
Input: s = "cbbd"
Output: "bb"
```
Example 3:
```
Input: s = "a"
Output: "a"
```
Example 4:
```
Input: s = "ac"
Output: "a"
 ```

Constraints:
```
1 <= s.length <= 1000
s consist of only digits and English letters.
```

-----
# 解法
把原字符串两侧用同样长度的无效值填充，然后把原来的字符串逆序，从第一个位置开始进行相等计算，连续出现相等情况最多的是