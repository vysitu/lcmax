[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/)

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:
```
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
```
Example 2:
```
Input: n = 1, bad = 1
Output: 1
 ```

Constraints:
```
1 <= bad <= n <= 231 - 1
```

-----
# 解法
我知道用黄金分割（0.618）理论上效率更高，但是我没弄好。分成十段，逐个推理的方法也搞砸了。最后改用了二分法过了。
这个波浪线表达在python3里面好像会出现奇怪的问题：if ~isBadVersion(x) 并不能正确的把True 变成False。

-----
# Python3
```python3
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        mid = int(n/2)
        if isBadVersion(mid):
            p2 = mid
            p1 = 1
        else:
            p1 = mid
            p2 = n
            print(p1, p2)
        if n <= 10:
            for i in range(1,n+1):
                if isBadVersion(i):
                    return(i)
        while p2 - p1 > 1:
            midpoint = int((p1+p2)/2)
            print(midpoint)
            if isBadVersion(midpoint):
                p2 = midpoint
            else:
                p1 = midpoint
            if p2 -p1 <= 1:
                return(p2)
                break

Runtime: 35 ms              (24.22%)
Memory Usage: 14.2 MB

# 高分答案其实也是二分法，不过代码要简洁很多。
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        
        return right
```