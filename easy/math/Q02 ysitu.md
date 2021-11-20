[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/)



Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:
```
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
```
Example 2:
```
Input: n = 0
Output: 0
```
Example 3:
```
Input: n = 1
Output: 0
 ```

Constraints:
```
0 <= n <= 5 * 106
```

-----
# 解法
循环，对每一个数字i使用质数表里面所有小于根号（i）的值，如果能整除的话i就不是质数。
选根号是因为如果能被大于根号i的值整除（比如，i整除大于根号i的j，得到k），那么k肯定是小于根号i的，所以取到小于根号i的那个k的时候就能发现i不是质数了。

但是！
我本来写的版本，在python里面运行较大数字的时候通不过，超时了。
这似乎是因为python对于列表的append处理是先遍历一遍列表再在最后添加一个元素。
所以先初始化一个空列表更好！？

# Python3
```python3
# 网友的高效率版本
import math
class Solution:
    def countPrimes(self,n):
        if n<3: return 0;
        primes=[1]*(n//2)
        for i in range(3,int(math.sqrt(n))+1,2):
            if primes[i//2]:primes[i*i//2::i]=[0]*((n-i*i-1)//(2*i)+1);
        return sum(primes)

# 我的低效率版本
def countPrimes(n: int) -> int:
    if n <= 2:
        return 0
    primes = [2]
    for i in range(3,n):
        isprime = True
        for p in primes:
            if p **2 > i:
                break
            if i % p == 0:
                isprime = False
                break  #is not prime
        if isprime:
            primes.append(i)
    return(primes)

# 我的改良版本
def countPrimes(n: int) -> int:
    if n <= 2:
        return 0
    primes = [0,0,1]+([0]*(n-3))
    for i in range(3,n,2):
        isprime = True
        for p in range(3, int(n**0.5) +1):
            if p**2 > i:
                break
            if i % p == 0:
                isprime = False
                break  #is not prime
        if isprime:
            primes[i] = 1
    return(sum(primes))

```