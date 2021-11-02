[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/)



You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
Example 3:

Input: matrix = [[1]]
Output: [[1]]
Example 4:

Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]
 

Constraints:

matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

-----
# 解法
这个题我没有清楚的头绪，只是觉得可以用反射的方法来简化。    
看了答案之后发现确实可以通过反射来做，而且可以通过多个函数来让整个流程显得非常清晰。     

# Python3
```python3
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            matrix[i] = matrix[i][::-1]

Runtime: 36 ms, faster than 73.16% of Python3 online submissions for Rotate Image.
Memory Usage: 14.3 MB, less than 29.22% of Python3 online submissions for Rotate Image.
```

# 附加题
https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
