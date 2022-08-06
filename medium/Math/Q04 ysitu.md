[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/818/)




Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:
```
Input: x = 2.00000, n = 10
Output: 1024.00000
```
Example 2:
```
Input: x = 2.10000, n = 3
Output: 9.26100
```
Example 3:
```
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 ```

Constraints:
```
-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
```

-----
# 解法
我觉得这个题是典型的，学Python的完全不应该遇到的问题，更别说是中等难度下了。
在C或者Java里面可能还会需要手动弄一个函数来处理这个，但是在Python里面，甚至连math库都不需要导入就可以解决了。题目里面也没说不能用自带的。

Python里面的幂计算就是2个乘号。

# Python3
```python3
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return(x**n)

```