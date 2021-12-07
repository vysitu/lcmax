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


Solutions:
```
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        res = ''
        n = len(min(strs))
        
        for i in range(n):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return res
            res += strs[j][i]
            
        return res

Runtime: 28 ms
Memory Usage: 14.4 MB
```