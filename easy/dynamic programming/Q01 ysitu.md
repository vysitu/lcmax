[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/)

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```
Example 2:
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 ```

Constraints:
```
1 <= n <= 45
```

-----
# 解法
从n-2的位置往上，可以一次两步；从n-1的位置往上，只能一次一步。从n-2的位置往上当然也可以连续跨两次“一步”，但是跨了一步之后其实就变成了n-1的位置了。
所以这个其实是斐波那契数列（F(n) = F(n-1)+F(n-2)），但是我的方法又TM超时了。

# Python3
```python3
# 斐波那契数列的方法
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return(1)
        elif n == 2:
            return(2)
        elif n >= 3:
            return(self.climbStairs(n-1)+ self.climbStairs(n-2))

# 看了其他人的提交之后意识到，斐波那契数列可以直接在函数里面生成，不需要递归……
class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [1,2]
        if n <= 2:
            return(fib[n-1])
        elif n >= 3:
            for i in range(n-2):
                fib.append(fib[i]+fib[i+1])
            return( fib[-1])

Runtime: 33 ms              (31.80%)
Memory Usage: 14.1 MB       (72.82%)
```