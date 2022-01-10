[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/)



Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:
(Figure 1)
```
Input: root = [2,1,3]
Output: true
```
Example 2:
(Figure 2)
```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 ```

Constraints:
```
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
```

# 解法
抄的网友答案。后面我都懒得写这句了，凡是树形结构的都是先看网友答案的。
- 有几种方法可以处理这类问题：Inorder Traversal, Pre-order Traversal, Post-order Traversal。
- BST(Binary Search Tree) 有一个特点就是，如果把它严格按照左-中-右的顺序拼接，那么可以看出是一定左<中<右的，或者说：

        1中    
      /     \    
    2左       2中    
  /    \     /   \    
3左1   3左2 3右1   3右2    

- 因为BST的每个分支也是BST，那么2左<1中<2右，而3左2=不一定=小于1中



# Python3
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = []
        self.inOrderGet(root, output)
        for i in range(len(output)-1):
            if output[i] >= output[i+1]:
                return False
        return(True)
        
    def inOrderGet(self, root, output):
        if root is None:
            return
        self.inOrderGet(root.left, output)
        output.append(root.val)
        self.inOrderGet(root.right, output)
```