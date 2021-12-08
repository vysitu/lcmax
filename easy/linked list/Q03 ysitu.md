[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/)



Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:
(Figure 1)
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```
Example 2:
(Figure 1)
```
Input: head = [1,2]
Output: [2,1]
```
Example 3:
```
Input: head = []
Output: []
 ```

Constraints:
```
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 ```

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

-----
# 解法
这个有空可以探讨一下。我觉得似乎直接涉及到链表的创建了。可能又要看别人答案了。

第一遍刷，先抄了个答案，加了些注释，以后再看递归的版本。
这个循环的办法本质上就是两个指针，前面那个指向没动过的数据，后面一个指针（其实是一组两个）进行next指向对象的交换。

[网友答案链接](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/discuss/58127/Python-Iterative-and-Recursive-Solution)

# Python3
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # output = head.copy()
        prev = None  # the last node points to None
        while head:
            current = head    # the back pointer moves forward
            head = head.next  #the front pointer points to unchanged data
            current.next = prev #the back pointer points back to the previous node
            prev = current   # the back pointer moves forward
        return(prev)
```