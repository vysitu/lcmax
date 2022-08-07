[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/821/)




Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:
```
Input: numerator = 1, denominator = 2
Output: "0.5"
```
Example 2:
```
Input: numerator = 2, denominator = 1
Output: "2"
```
Example 3:
```
Input: numerator = 2, denominator = 3
Output: "0.(6)"
```
Example 4:
```
Input: numerator = 4, denominator = 333
Output: "0.(012)"
```
Example 5:
```
Input: numerator = 1, denominator = 5
Output: "0.2"
 ```

Constraints:
```
-231 <= numerator, denominator <= 231 - 1
denominator != 0
```


# 解法
用的传统的方法，速度较慢，但是更好理解。
leetcode本来是可以灵活处理多种表达，结果7/12明明是0.58(3)，居然不允许写成0.583(3)。明明之前4/333都可以写成0.012(012)这样的。对此我只能说QTMD。

不过用暴力的方法处理重叠部分还是有点不妥，以后可能要寻求更妥善的处理方式。

我后来看了一下讨论区，似乎很多人都是用字典的方法来解决的。

优化：把判断newa出现次数的那个部分移动到newa存在于a_list中的判断分支中，能节约将近一半的时间。之前是115ms左右。

# Python3 
```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        a = numerator
        b = denominator
        
        # 得到正负情况，然后转换成两者都为正的情况来处理
        sign = '-' if a/b<0 else ''
        a = abs(a); b = abs(b)

        intstr = str(a//b)   # 取整数部分，检查是否有小数
        # 如果没有小数部分，直接返回
        if a % b == 0:
            return sign + intstr

        # 如果有小数部分，一直把剩余部分乘以10并取小数，直到为0或者出现重复的非0数字
        else:
            newa = a    # 每次循环，用之前的余数部分作为新的a
            fracstr = ''   
            frac_list = []  # 不循环的小数部分
            rep_list = []   # 循环的小数部分
            a_list = []     # 分子之前是否已经出现过？出现过则表明开始循环
            while newa % b != 0:   # 如果发生整除，则中断循环
                a_list.append(newa)     # 记录分子是否出现过
                newa = (newa % b) * 10  # 新的分子是余数小数点向左偏移一位(*10)，小数向右移动一位
                fracstr = str(newa // b)  # 取的整数部分其实是第一位小数
                if newa in a_list:   # 如果newa出现不足2次但是在a_list，表明正在循环中
                    if a_list.count(newa) == 2:  # 如果新的a已经出现过两次，
                        break                #表明rep_list已经纪录到了一整个循环，中断循环
                    rep_list.append(fracstr)
                else:               # 否则并没有在循环中
                    frac_list.append(fracstr)
            if len(rep_list)>0:           # 有循环的部分
                repstr = f'{"".join(rep_list)}'   # 循环刚开始的那一次因为newa不在a_list，
                fracout = f'{"".join(frac_list)}'  # 所以会被当成不循环的部分
                fracout = fracout.replace(repstr, '')  # 这时候就要从不循环的部分里把它去掉
                return sign + intstr + '.' + fracout + f'({repstr})' 
            else:
                return sign + intstr + '.' + f'{"".join(frac_list)}' 

```
Runtime: 66 ms          (12.53%)
Memory Usage: 14.2 MB
