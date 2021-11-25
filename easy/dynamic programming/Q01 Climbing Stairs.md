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

Solution:
```
This is Fibonacci Number->F(n) = F(n - 2) + F(n - 1) 

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        res = [0] * n
        
        res[0], res[1] = 1, 2
        
        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]
            
        return res[-1]

O(n), O(n)
```