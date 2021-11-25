[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/)



Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:
(Fig not included here)
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```
Example 2:
```
Input: head = [1], n = 1
Output: []
```
Example 3:
```
Input: head = [1,2], n = 1
Output: [1]
 ```

Constraints:
```
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 ```

Follow up: Could you do this in one pass?

-----
# 解法
双指针法。
前面那个指针先运行n次，指向第n个节点；
然后后面那个指针开始和前面那个一起动；
前面那个节点循环到最后一个的时候停下来，后面那个也停下来；
后面那个指针使用p2.next = p2.next.next，跳过一个节点，就相当于删除了那个节点。
然后返回原来的链表。

说起来很简单，但是Python写了半天弄不出来，失去耐心了。

网友答案：
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

```