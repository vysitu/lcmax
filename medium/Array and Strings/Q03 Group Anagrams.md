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

Solutions:
```
这是自己硬写出来的TLE，蠢就一个字。
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        list_1 = [''] * len(strs) 
        for i in range(len(strs)):
            list_1[i] = sorted(strs[i])

        new_list = []
        for ele in list_1:
            if ele not in new_list:
                new_list.append(ele)

        res = [[] for xx in range(len(new_list))]

        for i in range(len(new_list)):
            for j in range(len(strs)):
                if sorted(strs[j]) == new_list[i]:
                    res[i].append(strs[j])
        
        return res

这是网上的妙计。mapping & dict真是好东西。
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        
        for ele in strs:
            key = tuple(sorted(ele))
            dic[key] = dic.get(key, []) + [ele]
            
        return dic.values()
```