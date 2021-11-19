[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/721/)




Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:
```
Input: s = "()"
Output: true
```
Example 2:
```
Input: s = "()[]{}"
Output: true
```
Example 3:
```
Input: s = "(]"
Output: false
```
Example 4:
```
Input: s = "([)]"
Output: false
```
Example 5:
```
Input: s = "{[]}"
Output: true
 ```

Constraints:
```
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
```

-----
# 解法
转换成列表，然后循环。因为只有括号，没有其他东西，所以从最贴近的一对括号开始，肯定是'[]'这种，换成列表就是 i = i+1

# Python3
```python3
class Solution:
    def isValid(self, s: str) -> bool:
        s1 = list(s)
        while True:
            found = False
            for i in range(len(s1)-1):
                if i >= len(s1) -1:
                    break
                if (s1[i] == '{') and (s1[i+1] == '}'):
                    s1.pop(i)
                    s1.pop(i)
                    found = True
                    break
                if (s1[i] == '[') and (s1[i+1] == ']'):
                    s1.pop(i)
                    s1.pop(i)
                    found = True
                    break
                if (s1[i] == '(') and (s1[i+1] == ')'):
                    s1.pop(i)
                    s1.pop(i)
                    found = True
                    break
            if (found):
                continue
            if ~found:
                print(s1)
                break
                
        if len(s1)>0:
            return(False)
        else:
            return(True)

Runtime: 1548 ms        (运行时间极长，都不知道排到哪里去了)
Memory Usage: 14.5 MB
```