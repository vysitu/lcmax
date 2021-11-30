[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/819/)




Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

Example 1:
```
Input: x = 4
Output: 2
```
Example 2:
```
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 ```

Constraints:
```
0 <= x <= 231 - 1
```

-----
# 解法
用的是去凑的方法。

但是凑数的时候也可以取一点巧。

- 注意到，10的平方是100， 100的平方是10000，依此类推。也就是说，输入的数的位数每增加两位，所需的平方根会增加一位——且是3，5，7这样的奇数位数时适用。
- 再注意到，3的平方是9（接近10），30的平方是900（接近1000），所以在位数即将变成偶数位数时，可以从3开头的数来尝试。
- 采用这两点来设置开始猜的数，有助于加快猜测的速度。

# Python3
```python3
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return(0)
        n = len(str(x))
        tencount = (n+1)//2
        threecount = (n+1)%2
        startnum = (10**(tencount-1))*(1+threecount*2)
        sq = startnum * startnum
        while True:
            startnum += 1
            sq = startnum * startnum
            if sq > x:
                startnum -= 1
                break
        return(startnum)
# 内存上有些可以优化的部分，但是我看了一眼速度排名之后发现靠前的似乎都是用的两个星号之类的……那就不如保留原样，方便你阅读。

```