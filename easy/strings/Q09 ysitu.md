[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/)


Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```
Example 2:
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 ```

Constraints:
```
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
```


-----
# 解法
用zip。这题我也是抄的答案。今天这两个debug真的把我恶心坏了，操。明明写的和其他人的差不多，就是要出毛病。
这个题逻辑本来也很简单，对每个str都检查第x个元素，如果超出长度则返回目前为止所有元素，如果和当前元素不符则返回当前元素为止的所有元素。
大家都和第一个对比就行，反正只要有一个和第一个str的x元素不一样就可以中断循环了。
就是TM写成代码要扯皮。

- 日决完了之后代码可以运行了……？
  

# Python3
```python3
# 网友：
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

# 我的解法。不优雅，但是直白，且最终还是能用：

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        count = 0
        if (strs[0] == ''):
            return('')
        for i in range(len(strs[0])):
            curr = strs[0][i]
            for s in strs:
                if (i >= len(s)):
                    return(strs[0][:count])
                if (s[i] != curr) :
                    return(strs[0][:count])
            count += 1
        return(strs[0][:count])

Runtime: 32 ms          (83.66%)
Memory Usage: 14.4 MB
```