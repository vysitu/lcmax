[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/820/)




Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

Example 1:
```
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
```
Example 2:
```
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
```
Example 3:
```
Input: dividend = 0, divisor = 1
Output: 0
```
Example 4:
```
Input: dividend = 1, divisor = 1
Output: 1
 ```

Constraints:
```
-231 <= dividend, divisor <= 231 - 1
divisor != 0
```

-----
# 解法
用暴力直接一个个的加上去会TLE（Time Limit Exceeded）。

看了网友的答案，确实用到了指数增加推测值来节约时间的方法，但是看了网友的设计，真TM的妙啊

草

# Python3
```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 同符号，if的括号得到的是True，sign就是1
        # 符号相反，if得到的False，最终得到-1
        sign = 1 if ((dividend > 0) is (divisor > 0)) else -1 
        divisor, dividend = abs(divisor), abs(dividend)  # 取绝对值再计算
        output = 0
        while dividend >= divisor:    # 除数大于被除数就输出0了
            temp = divisor            # 
            shift = 1                 # 
            while dividend >= temp:   # 
                dividend -= temp      # 被除数减去temp
                temp <<= 1            # 左移一位就是乘以2，两位就是乘以2的2次方
                output += shift       # 偏移量其实就是除的部分结果
                shift <<= 1           # 增加偏移量，如果temp偏移过头，无法计算
        result = output * sign        # 乘以符号得到结果，之后判断范围
        result = result if result < 2**31-1 else 2**31-1
        result = result if result > -1*(2**31) else -1*(2**31)
        return(result)

```
