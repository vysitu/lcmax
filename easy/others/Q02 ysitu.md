[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/)




The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 

Example 1:
```
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
```
Example 2:
```
Input: x = 3, y = 1
Output: 1
 ```

Constraints:
```
0 <= x, y <= 231 - 1
```

-----
# 解法
全部转成二进制，再转成字符串，然后补齐前面的位数，再逐位对比是否相同，不相同就 count += 1

# Python3
```python3
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if (x > 2**31-1) or (y > 2**31-1):
            return(None)
        xs = str(bin(x))[2:]
        ys = str(bin(y))[2:]
        newxs = '0'*(32-len(xs))+xs
        newys = '0'*(32-len(ys))+ys
        count = 0
        for i in range(32):
            xbit = newxs[i]
            ybit = newys[i]
            if xbit != ybit:
                count += 1
        return(count)

Runtime: 32 ms              (62.77%)
Memory Usage: 14.3 MB       (44.54%)
```