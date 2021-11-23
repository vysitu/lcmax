(Link to Question)[https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/]


# 解法
这个题目好像有问题，都不知道要删除哪一个，怎么搞啊？
看了答案说是直接提供一个功能，把本节点指向下一个节点就可以了。
这个我还算好理解，不过就是觉得有点憨批。
网友说的，把这个节点换成下一个，然后对中间那个节点say fxxk you
我觉得太形象了。

# Python3
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

# 计时意义不大
```