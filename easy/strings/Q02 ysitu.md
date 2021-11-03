[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/)

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:
```
Input: x = 123
Output: 321
```
Example 2:
```
Input: x = -123
Output: -321
```
Example 3:
```
Input: x = 120
Output: 21
```
Example 4:
```
Input: x = 0
Output: 0
 ```

Constraints:
```
-231 <= x <= 231 - 1
```

-----
# 解法 
变成字符串，然后反转就行了。注意处理负号。     

# Python3
```python3
class Solution:
    def reverse(self, x: int) -> int:
        xstr = str(x)
        if xstr[0] == '-':      #处理负号
            xrev = -1*int(xstr[1:][::-1])
        else:
            xrev = int(xstr[::-1]) #调转字符串顺序，然后转成整型
        if abs(xrev) > 2**31:   #题目要求的范围
            xrev = 0
        return(xrev)

Runtime: 32 ms          (78.38%)
Memory Usage: 14.3 MB   (44.74%)
```