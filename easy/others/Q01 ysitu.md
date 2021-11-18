[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/565/)


Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 

Example 1:
```
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
```
Example 2:
```
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
```
Example 3:
```
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 ```

Constraints:
```
The input must be a binary string of length 32.
 ```

Follow up: If this function is called many times, how would you optimize it?

-----
# 解法
用bin()转成二进制，转成字符串型，再转成列表，然后计算"1"的数量。。。
二进制的表示是0b1011这样的，前面的0b转成字符串不影响"1"的数量，所以可以省略去除"0b"的步骤。

# Python3
但是，去掉"0b"之后似乎可以提高速度。
```python3
class Solution:
    def hammingWeight(self, n: int) -> int:
        s = list(str(bin(n)))
        return(s.count('1'))
Runtime: 28 ms          (87.71%)
Memory Usage: 14.3 MB

class Solution:
    def hammingWeight(self, n: int) -> int:
        s = list(str(bin(n))[2:])
        return(s.count('1'))
Runtime: 24 ms          (96.77%)
Memory Usage: 14.2 MB   (39.70%)
```
