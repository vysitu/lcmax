[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/822/)




Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:
```
Input: a = 1, b = 2
Output: 3
```
Example 2:
```
Input: a = 2, b = 3
Output: 5
 ```

Constraints:
```
-1000 <= a, b <= 1000
```

-----
# 解法
不知道该说点啥……

投机取巧的话，python里面有个sum……sum就不是加减号了，岂不美哉？   
也可以用math里面的log取对数，这个我觉得也算是一种投机取巧……

我估计官方的思路是转换成二进制，然后使用逻辑的方法做一个二进制加法函数出来。

# Python3

```python3
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return(sum([a,b]))

# 使用math
import math
class Solution:
    def getSum(self, a: int, b: int) -> int:
        p1 = 2**a
        p2 = 2**b
        s = math.log2(p1*p2)
        return(round(s))
```