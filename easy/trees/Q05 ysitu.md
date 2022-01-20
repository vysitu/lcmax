[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/)



Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 

Example 1:
(Figure 1a)
```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
(Figure 1b)
```
Example 2:
(Figure 2)
```
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
 ```

Constraints:
```
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
```

-----
# 解法
审题正确的话还是比较好理解的。

说白了就是两边的分枝深度差距不要太大。

每次都取中间那个值作为root，然后剩下的用递归的方法设置左右两边的分枝就可以了。

# Python
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:   #给定的列表为空或者节点为空
            return None
        mid = len(nums) // 2   #取中间的值
        root = TreeNode(nums[mid])  #创建当前的root节点
        #用递归的方法创建左边，对数组左边部分进行同样的处理
        root.left = self.sortedArrayToBST(nums[:mid])  
        root.right = self.sortedArrayToBST(nums[mid+1:]) #用递归的方法创建右边
        return root
```