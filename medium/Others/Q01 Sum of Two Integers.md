[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/822/)




Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:
```
Input: a = 1, b = 2
Output: 3
```
Example 2:
```
Input: a = 2, b = 3
Output: 5
 ```

Constraints:
```
-1000 <= a, b <= 1000
```

Solutions:
```
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a,b])
```