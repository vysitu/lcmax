[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/)




Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:
(Figure 1)
```
Input: head = [1,2,2,1]
Output: true
```
Example 2:
(Figure 2)
```
Input: head = [1,2]
Output: false
 ```

Constraints:
```
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 ```

Follow up: Could you do it in O(n) time and O(1) space?

-----
# 解法
我用了最普通的解法，并且我认为这个是一个简洁好懂的方案。

更关键的是，这好像是我完全凭自己解出来的第一道链表的题目，而且是直接在网页上就通过了！

小庆祝一下。

思路就是，不可能在不循环整个链表的情况下知道是不是对称，所以时间复杂度必然是O(n)往上。把每个节点的值存到list，就把整个问题转化成很容易解决的那种了。之后有时间可以思考一下如何用O(1)空间来解决这个问题。

# Python3
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        p = head
        while p.next is not None:
            vals.append(p.val)
            p = p.next
        vals.append(p.val)
        if vals == vals[::-1]:
            return(True)
        else:
            return(False)

Runtime: 808 ms         (66.22%)
Memory Usage: 47.5 MB   (18.11%)
```