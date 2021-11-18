[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/601/)




Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

(Figure 1)
 

Example 1:
```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```
Example 2:
```
Input: numRows = 1
Output: [[1]]
 ```

Constraints:
```
1 <= numRows <= 30
```

-----
# 解法

# Python3
```python3
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rowf = [[1], [1, 1], [1, 2, 1]]
        if numRows <= 3:
            return rowf[:numRows]
        else:
            rowout = rowf.copy()
            for i in range(numRows - 3):
                newrow = [1]
                for k in range(len(rowout[2+i])-1):
                    newrow.append(rowout[2+i][k]+rowout[2+i][k+1])
                newrow.append(1)
                rowout.append(newrow)
            return(rowout)

Runtime: 20 ms          (99.36%)
Memory Usage: 14.3 MB   (57.06%)
```