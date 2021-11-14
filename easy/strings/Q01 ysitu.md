(Link to Question)[]

Write a function that reverses a string. The input string is given as an array of characters s.

 

Example 1:
```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```
Example 2:
```
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 ```

Constraints:

- 1 <= s.length <= 105
- s[i] is a printable ascii character.


Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

-----
# 解法
1. 可以直接用[::-1]     
2. 也可以设置一个指针从后往前，另一个从前往后，然后交换指针指向的两个元素。   

# Python3
解法1
```python3
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

Runtime: 196 ms         (84.29%)
Memory Usage: 18.7 MB   (17.90%)
```
解法2     
内存占用更少的答案也是这个解法，不知道为什么他们的内存占用更少。
```python3
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #s[:] = s[::-1]
        n = len(s)
        for p1 in range(n):
            p2 = n-p1-1
            if p2<p1:
                break
            else:
                s[p1], s[p2] = s[p2], s[p1]

Runtime: 200 ms         (72.43%)
Memory Usage: 18.7 MB   (43.26%)
```
解法3
终极方案：s.reverse()   原地反转列表s，都不需要另外指定变量。