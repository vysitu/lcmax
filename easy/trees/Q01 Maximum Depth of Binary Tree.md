[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/)

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:

```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```
Example 2:
```
Input: root = [1,null,2]
Output: 2
```
Example 3:
```
Input: root = []
Output: 0
```
Example 4:
```
Input: root = [0]
Output: 1
 ```

Constraints:
```
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
```

-----
# 解法
**我是看了答案才知道有这种操作的。**

用递归的办法直接对每个分支都进行搜索，直到找到最后一个为止。在此期间每增加一层深度，返回值+1；在某一层如果没有值则返回0。这样搜索到最后，返回的值其实就是N层（每层一个1）和最后一层的0和。

# Python3
```python3
# 这个是比较符合我的编写风格的写法，从别人答案里改编过来的。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return(0)
        return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))
```