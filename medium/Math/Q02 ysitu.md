[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/816/)




Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:
```
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
```
Example 2:
```
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
```
Example 3:
```
Input: n = 0
Output: 0
 ```

Constraints:
```
0 <= n <= 104
 ```

Follow up: Could you write a solution that works in logarithmic time complexity?

-----
# 解法
这个题其实真的有一种小学奥数题，找规律的感觉。
硬乘肯定不行，一路乘到1e4肯定很长，估计什么整型都顶不住。
规律就是，任何时候都只有乘数的因数的部分包含10，尾数才会有更多的0。

同时注意到，10的质因数是2x5。例如，1乘到5，无论是2x5还是4x5，里面都包含了2和5。

所以重点是5！

再注意到，25这种是包含两个5的，类似的包含多个5的乘数之前的任何偶数都肯定包含了2，那么这些包含多个5作质因数的数肯定会增加对应数量的0。

写这么多是因为我一边看直播，一边花了很短的时间就想出来了，小自豪一下。

# Python3
```python3
class Solution:
    def trailingZeroes(self, n: int) -> int:
        output = 0
        for i in range(1,10):
            output += n//(5**i)
        return(output)

Runtime: 32 ms          (78.68%)
Memory Usage: 14.3 MB   (45.96%)
```