[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/)

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:
```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```
Example 2:
```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
```
Example 3:
```
Input: digits = [0]
Output: [1]
Explanation: The array represents the integer 0.
Incrementing by one gives 0 + 1 = 1.
Thus, the result should be [1].
```
Example 4:
```
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 ```

Constraints:
```
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
```

-----
# 解法
先转成int，这样相加就不需要人工操作；再转回str，然后拆开……

# Python3
```python3
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n1 = []
        for i in digits:
            n1.append(str(i))
        i1 = int(''.join(n1))
        i2 = i1+1
        n2 = str(i2)
        n3 = []
        for i in n2:
            n3.append(int(i))
            
        return(n3)

Runtime: 28 ms          (92.61%)
Memory Usage: 14.4 MB   ()
```