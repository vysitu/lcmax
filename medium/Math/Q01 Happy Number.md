[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/815/)




Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:
```
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```
Example 2:
```
Input: n = 2
Output: false
 ```

Constraints:
```
1 <= n <= 231 - 1
```

Constraints:
```
自家解法
class Solution:
    def isHappy(self, n: int) -> bool:
        temp = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n) ])
            if n in temp:
                return False
            else:
                temp.add(n)
        
        return True
Runtime: 36 ms
Memory Usage: 14.4 MB

大神解法，并不是说ta的算法快些。我单纯想感慨一下这个代码习惯是真的好
class Solution:
    def isHappy(self, n: int) -> bool:
        assert(1<=n<(2**31)-1, 'Please enter a number between 1 and (2**31) - 1')
        

        attempt = 0
        seen = set()
        while n != 1 and attempt < 1000 and n not in seen:
            seen.add(n)
            squaredListDigits = list(map(lambda x: int(x)**2,str(n)))
            n =  sum(squaredListDigits)
            attempt += 1
            
        return True if n == 1 else False
```