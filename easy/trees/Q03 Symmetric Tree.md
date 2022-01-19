[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/)



Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:
(Figure 1)
```
Input: root = [1,2,2,3,4,4,3]
Output: true
```
Example 2:
(Figure 2)
```
Input: root = [1,2,2,null,3,null,3]
Output: false
 ```

Constraints:
```
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 ```

Follow up: Could you solve it both recursively and iteratively?

Solutions:
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        stack = [(root.left, root.right)]
        
        while len(stack) > 0:
            left, right = stack.pop()
            
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
            
        return True
```