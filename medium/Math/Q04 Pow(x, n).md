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

Solutions:
```
“递龟”
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def recursion(base = x, y = abs(n)):
            if y == 0:
                return 1
            elif y % 2 == 0:
                return recursion(base * base, y // 2)
            else:
                return base * recursion(base * base, (y - 1) // 2)
            
        if n >= 0:
            return float(recursion())
        else:
            return 1/recursion()
Runtime: 32 ms
Memory Usage: 14.3 MB
```