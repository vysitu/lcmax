[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/)




Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

 

Example 1:
(Figure 1)
```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```
Example 2:
(Figure 2)
```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 ```

Constraints:
```
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 ```

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

-----
# 解法
我这个解法应该算是O(m+n)的？

我只需要一个列表来储存所有行里出现过0的index。第一次循环，获得0的index并且把出现过0的行设置为全0；第二次循环是一个嵌套循环，把每一行里的index依次设置为0。

# Python3
```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rownum = len(matrix)    #num of rows
        colnum = len(matrix[0]) #num of cols
        col_zero = []
        for row_ind, row in enumerate(matrix):
            if 0 in row:
                col_zero.extend([ind for ind, x in enumerate(row) if x == 0])  #record all 0s
                matrix[row_ind] = [0] * colnum  #set the whole row to 0
        col_zero = list(set(col_zero))
        for row_ind, row in enumerate(matrix):
            for col_ind in col_zero:
                matrix[row_ind][col_ind] = 0
# 耗时和其他答案比挺多的，但是其他答案我看还没有我这个直观，而且循环次数巨TM多。
Runtime: 231 ms         (5.77%)
Memory Usage: 15.1 MB   (46.98%)
```