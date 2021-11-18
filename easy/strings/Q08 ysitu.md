[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/)



The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251":


Given a positive integer n, return the nth term of the count-and-say sequence.

 

Example 1:
```
Input: n = 1
Output: "1"
Explanation: This is the base case.
```
Example 2:
```
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
 ```

Constraints:
```
1 <= n <= 30
```

-----
# 解法
其实方法很简单，就是迭代，可以把函数搞个递归，也可以不搞。然后弄一个index，随着index移动的时候判断是不是和前一个元素相同，是的话就加长当前str，不是的话就把之前的str放到list里面。最后对list的每个元素求长度，取其值（比如元素的第一个char），就可以了。
但是这题真TM把我恶心坏了，怎么debug都理不清楚。抄的网友答案。

# Python3
```python3
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        seq = [1]
        output = []
        while n > 1:
            temp = []
            curr = seq[0]
            c = 1
            for i in range(1, len(seq)):
                if seq[i] != curr:
                    temp.append(c)
                    temp.append(curr)
                    curr = seq[i]
                    c = 1
                else:
                    c += 1
            temp.append(c)
            temp.append(curr)
            seq = temp
            n -= 1
        for i in seq:
            output.append(str(i))
        return ''.join(output)


# 递归：
class Solution:
    l = ["1"] + [None] * 29
    def countAndSay(self, n: int) -> str:
        if not self.l[n-1]:
            x = self.countAndSay(n-1)
            count, char = 1, x[0]
            res = []
            for i in range(1, len(x)):
                if x[i] != char:
                    res.append(str(count))
                    res.append(char)
                    char = x[i]
                    count = 1
                else:
                    count += 1
            res.append(str(count))
            res.append(char)
            self.l[n-1] = "".join(res)
        return self.l[n-1]
```






