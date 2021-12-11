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

Constraints:
```
自制解法献丑了，强行算。
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0 
            
        res = 1
        for i in range(1, n + 1):
            res *= i

        temp = str(res)
        count = 0
        
        while temp[-1] == '0':
            count += 1
            temp = temp[:-1]

        return count


```