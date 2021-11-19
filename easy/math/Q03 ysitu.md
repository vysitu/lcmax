[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/)




Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:
```
Input: n = 27
Output: true
```
Example 2:
```
Input: n = 0
Output: false
```
Example 3:
```
Input: n = 9
Output: true
```
Example 4:
```
Input: n = 45
Output: false
 ```

Constraints:
```
-231 <= n <= 231 - 1
 ```

Follow up: Could you solve it without loops/recursion?

-----
# 解法
无脑循环流……
不让用循环和递归，那你TM倒是让我用对数啊，对数发明出来不就是干这个的？

# Python3
```python3
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if (n == 1) or (n==3):
            return(True)
        if n == 2:
            return(False)
        while n>3:
            if n % 3 == 0:
                n /= 3
            else:
                return(False)
            if n == 3:
                return(True)
            else:
                continue
        return(False)

Runtime: 76 ms          (75.06%)
Memory Usage: 14.1 MB   (77.74%)
```

# 卧槽
还真可以用对数，直接在最开始导入python自己的math包就行。但是这么搞的速度反而不如直接硬循环……
而且需要加入各位数字的和验证，避免浮点数的误差导致无法正确判断是否是3的倍数。

```python3
import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if (n <= 0):
            return(False)
        if n ==1:
            return(True)
        comp = (math.log(n)/math.log(3)) % 1
        if abs(comp - round(comp)) < 1e-6:
            res = 0
            for i in list(str(n)):
                res = res+int(i)
            if abs(res % 3) < 1e-6:
                return(True)
        else:
            return(False)

Runtime: 92 ms          (40.52%)
Memory Usage: 14.4 MB
```