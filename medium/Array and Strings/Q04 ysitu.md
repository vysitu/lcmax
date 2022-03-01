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
双指针法。移动靠前的指针，如果出现重复的，就把重复的那个位置变成靠后的指针的位置，并且记录最新的字符串长度。

