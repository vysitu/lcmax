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

# 草稿
费了半天劲发现审题没审好，先记一下草稿，这个是测试是不是每个分支都完整的。

```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if sum([(root.left is None), (root.right is None)]) == 1:  
            return False
        elif sum([(root.left is None), (root.right is None)]) == 2:  
            return True
        elif sum([(root.left is None), (root.right is None)]) == 0:
            return self.isSymmetric(root.left) and self.isSymmetric(root.right)
```

# 解法
先抄答案吧。。。

# Python 递归
```python
  def isSymmetric(self, root):
      if root is None:
          return True
      stack = [(root.left, root.right)]  #同时探索左边分枝和右边分枝
      while stack:
          left, right = stack.pop()
          if left is None and right is None: #两边都到头了
              continue
          if left is None or right is None:  #有一侧先到头了
              return False
          if left.val == right.val:
              stack.append((left.left, right.right))  #对称的添加
              stack.append((left.right, right.left))  #对称的添加
          else:
              return False
      return True
```
# Python 迭代
```python
def isSymmetric(self, root):
    last = [root]
    while True:
        if not any(last):
            return True
        current = []
        for node in last:
            if node is not None:
                current.append(node.left)
                current.append(node.right)
        if not self.is_list_symmetric(current):
            return False
        else:
            last = current
    
def is_list_symmetric(self, lst):
    head, tail = 0, len(lst) - 1
    while head < tail:
        h, t = lst[head], lst[tail]
        head += 1
        tail -= 1
        if h == t == None:
            continue
        if None in (h, t) or h.val != t.val:
            return False
    return True
```