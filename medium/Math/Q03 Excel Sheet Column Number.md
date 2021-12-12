[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/817/)




Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:
```
Input: columnTitle = "A"
Output: 1
```
Example 2:
```
Input: columnTitle = "AB"
Output: 28
```
Example 3:
```
Input: columnTitle = "ZY"
Output: 701
```
Example 4:
```
Input: columnTitle = "FXSHRXW"
Output: 2147483647
 ```

Constraints:
```
1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
```

Solutions:
```
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        res = 0
        
        for i in range(n):
            res *= 26
            res += (ord(columnTitle[i]) - ord('A') + 1)
            
        return res
        
Runtime: 32 ms
Memory Usage: 14 MB
```