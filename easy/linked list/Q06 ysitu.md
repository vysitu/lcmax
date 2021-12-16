[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/)




Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:
(Figure 1)
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```
Example 2:
(Figure 2)
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```
Example 3:
(Figure 3)
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 ```

Constraints:
```
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 ```

Follow up: Can you solve it using O(1) (i.e. constant) memory?

-----
# 解法
抄的答案。

用双指针法，一个指针移动速度是另一个的两倍【快的被叫做runner，慢的被叫做walker】，如果有循环，那么移动快的那个会进入循环重复循环，直到移动慢的那个赶上，并且确认两者相等。因为慢的那个每次只前进一个位置，所以如果有循环的话两者最终总会相交。没有循环的话，快的那个到头了就可以宣布循环结束了。

确实是个巧妙且简介的办法。

# Python3
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        step1 = step2 = head
        if head is None:
            return(False)
        while (step2.next is not None) and (step2.next.next is not None):
            step1 = step1.next
            step2 = step2.next.next
            if step1 == step2:
                return(True)
        return(False)
```