[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/)




Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```
Example 2:
```
Input: strs = [""]
Output: [[""]]
```
Example 3:
```
Input: strs = ["a"]
Output: [["a"]]
 ```

Constraints:
```
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
```

-----
# 解法
我的第一个解法需要改进。

目前的方法是O(N)的，我觉得已经很有效了，但是网友拿出来一个defaultdict的东西，结果总速度比我这个快七八倍。然后用字典的values功能也可以大幅提速。

我的第一种解法是使用两个列表，一个记录已经出现的值，一个记录分组的输出。对于已经出现的值的判断，我是通过转换成列表--排序--转换回字符串的方式进行的。我认为这个部分没有多少改良空间。但是用字典似乎能够提高效率。

# Python3
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        inorder = []
        output = []
        for s in strs:
            a = list(s)     #变成list方便排序
            a.sort()        #排序
            a = ''.join(a)  #变回str
            if a in inorder:
                output[inorder.index(a)].append(s)
            else:
                inorder.append(a)
                output.append([s])
        return(output)
Runtime: 668 ms         (大幅超出平均用时)
Memory Usage: 17.8 MB   (57.91%)
Runtime: 576 ms         (大幅超出平均用时)
Memory Usage: 17.2 MB   (78.67%)
```
### 一开始我竟然忘了把''.join(a)赋值给a，结果排序用的是列表相等，时间668ms那次。


## Python3 改进方案
- 使用字典
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        inorder = []
        output = {}
        for s in strs:
            a = list(s)
            a.sort()
            a = ''.join(a)
            if a in inorder:
                output[a].append(s)
            else:
                inorder.append(a)
                output[a] = [s]
        return(output.values())

Runtime: 556 ms
Memory Usage: 17.5 MB   (70.43%)
```