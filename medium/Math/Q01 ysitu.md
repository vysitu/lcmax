[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/815/)




Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:
```
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```
Example 2:
```
Input: n = 2
Output: false
 ```

Constraints:
```
1 <= n <= 231 - 1
```

-----
# 解法
据说去微软面试只要说一句“用暴力解”就会被拒……

暴力！暴力！暴力！

Violence solves everything -- Katarina

这个题目主要是注意审题。题目里面说了会是endlessly loop in a list而不是归1，那么只要元素开始重复，或者元素归1，就可以停止循环了。应对这种情况使用while循环比较方便。

# Python3
```python
class Solution:
    def isHappy(self, n: int) -> bool:
        elements = []
        while True:
            temp = 0
            for s in list(str(n)):  #给每一位数取平均，加在一起
                temp += int(s)**2
            n = temp
            if temp == 1:   #归1，退出循环，返回True
                return True
            elif temp not in elements:  #不归1，添加到一个总表，每次对比
                elements.append(temp)
            elif temp in elements:   #元素开始重复，那肯定就没法归1了，返回False
                print(elements)
                return False

Runtime: 36 ms          (63.61%)
Memory Usage: 14.1 MB   (75.87%)
```

