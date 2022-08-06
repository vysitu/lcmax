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

-----
# 解法
乍一看：

这个就是26个字母的进位制，其实就是27进制。因为数到第26个字母之后就只能进位了，所以就和数到9个字母之后要“逢十进一”一样，只是改成“逢27进1”而已。

写了一个框架之后发现A表示1，AA表示27，也就是说其实本质上是26进制，因为A除了在首位以外，其他位置都是表示“0”……

从答案的速度来看，我的思路应该算是对的了，具体如果面试的时候要手写可能有点麻烦，因为我这个解答其实是试出来的。只考思路的话，应该可以秒答了。

# Python3
```python3
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        output = 0
        for i in range(0,n):
            output += (ord(columnTitle[n-i-1])-64)*(26**i)
        return(output)

Runtime: 24 ms          (98.59%)
Memory Usage: 14.3 MB
```