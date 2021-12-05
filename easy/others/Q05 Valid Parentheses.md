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

Solutions
```
这个办法比较直观但是比较哈啤。从内到外把所有括弧移除。时间复杂度大于O（N）
class Solution:
    def isValid(self, strsInputs: str) -> bool:

        while '[]' in strsInputs or '()' in strsInputs or '{}' in strsInputs:
            strsInputs = strsInputs.replace('[]','').replace('()','').replace('{}','')
        
        if len(strsInputs) == 0:
            return True
        else:
            return False
Runtime: 40 ms
Memory Usage: 14.1 MB


利用stack先进后出的特性来解决问题, O(N)
class Solution:
    def isValid(self, strsInputs: str) -> bool:
        if len(strsInputs) % 2 == 1:
            return False
        
        stack = []
        mapping = {'(':')', '[':']', '{':'}'}
        
        for b in strsInputs:
            if b in mapping:
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if mapping[temp] != b:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

Runtime: 28 ms
Memory Usage: 14.4 MB
```
