[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/743/)



Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.
 

Example 1:
```
Input: n = 3
Output: ["1","2","Fizz"]
```
Example 2:
```
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
```
Example 3:
```
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 ```

Constraints:
```
1 <= n <= 104
```

-----
# 解法
这个没有什么技术含量，除了n=1的时候的处理，其他直接用%求余，然后看余数是不是0就行。
此外就是可以注意到，同时能被3和5整除其实就是能被15整除……这样可以节省一些判断的步骤。

# Python3
```python3
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(1,n+1):
            if i == 1:
                output.append('1')
                continue
            if i % 15 ==0:
                output.append('FizzBuzz')
            elif i%5 == 0:
                output.append('Buzz')
            elif i%3 == 0:
                output.append('Fizz')
            else:
                output.append(str(i))
        return(output)

Runtime: 40 ms          (84.91%)
Memory Usage: 15 MB     (67.40%)
```