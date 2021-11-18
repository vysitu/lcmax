[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/)




Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 

Example 1:
```
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
```
Example 2:
```
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 ```

Constraints:
```
The input must be a binary string of length 32
 ```

Follow up: If this function is called many times, how would you optimize it?

-----
# 解法
中规中矩的方法，直接转换成二进制，输出本身就是str型，直接去掉"0b"然后翻转，使用int(strobj, 2)来转换成二进制数

# Python3
```python3
class Solution:
    def reverseBits(self, n: int) -> int:
        nb = bin(n)[2:]
        nb = '0'*(32-len(nb))+nb
        return(int(nb[::-1], 2))

Runtime: 32 ms          (75.05%)
Memory Usage: 14.3 MB   (本来代码里有个print，浪费了一些资源)
```