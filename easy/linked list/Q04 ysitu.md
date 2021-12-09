[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/)




Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:
(Figure 1)
```
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
```
Example 2:
```
Input: l1 = [], l2 = []
Output: []
```
Example 3:
```
Input: l1 = [], l2 = [0]
Output: [0]
 ```

Constraints:
```
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
```

-----
# 解法
我觉得挺简单的。

分成表1和表2，从两个链表的第一个node（节点）开始，如果表2下一个节点的值大于

但是写的代码会遇到bug，说链表自身循环了。

我的第一版解法如下。

不知道是犯什么病。

看了网友答案之后，我的感觉是“这么憨批的办法也能通过！？”。毫无操作可言，ListNode(0)直接新建一个链表，这时候倒是不想省内存了哈。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        count = 0
        while p1:
            if p1.next.val >= p2.val:
                p1.next.val = p2.val
                p1.next.next = p1.next
                p2 = p2.next
                p1 = p1.next
            else:
                p1 = p1.next
            count += 1
            if count > 200: 
                break
        return(list1)
```

第二版

还是想用把一个表添加到另一个的办法。

会报错，因为两个链表都只有一个节点的时候，选择从哪个表添加到哪个表就是一个重要问题了。

只有一个节点还用尼玛个比的链表啊操！

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1f = list1
        p1b = list1
        p2 = list2
        if p1b is None:
            return(list2)
        while p1f and p2:
            if p1f.val < p2.val:
                p1b = p1f  #lag = 1
                p1f = p1f.next
            else:
                newnode = ListNode(p2.val, p1b.next)
                p1b.next = newnode
                p1b = p1b.next
                p2 = p2.next
        return list1

```


# Python3
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        output = p = ListNode(0)
        
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        p.next = p1 or p2
        return output.next
```