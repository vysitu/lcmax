[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/)



Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:
(Figure 1)
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```
Example 2:
```
Input: root = [1]
Output: [[1]]
```
Example 3:
```
Input: root = []
Output: []
 ```

Constraints:
```
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
```

-----
# 解法
用循环的方法来遍历，一个列表记录所有下一层的节点，另一个列表记录所有本层的节点的值。

我是这么想的……但是写出来通不过。看了网友的办法，也是这么解的。

# Python
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans, level = [], [root]  # ans记录节点的值，level记录下一层的节点
        if not root: 
            return([]) 
        while root and level:
            ans.append([node.val for node in level])
            LRpair = [(node.left, node.right) for node in level]
            # level = [leaf for LR in LRpair for leaf in LR if leaf]
            temp = []
            for node in level:
                temp.extend([node.left, node.right])  #下一层的所有节点
            level = [leaf for leaf in temp if leaf]   #去掉空节点
        return ans
```