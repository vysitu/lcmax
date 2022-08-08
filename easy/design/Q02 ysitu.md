[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/562/)



Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
 

Example 1:
```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 ```

Constraints:
```
-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
```

-----
# 解法
本来我还在设计用list来储存，每个数字是一个list里面的list，相当于二维数组，然后取出来的时候先从前面取，放进去也先从前面放。

结果看了答案，感觉智商被侮辱了我操。这个题确实也没说要从前面还是后面添加元素。然后也没说一定要搞list套list，直接用一个list就可以用python的自带方法解决问题了。

# Python3
```python3
class MinStack:

    def __init__(self):
        self.x = []

    def push(self, val: int) -> None:
        self.x.append(val)

    def pop(self) -> None:
        self.x.pop()

    def top(self) -> int:
        return(self.x[-1])

    def getMin(self) -> int:
        return(min(self.x))

# 速度并不快。速度快的答案我看似乎在做list的时候就要把最小值之类的先考虑进去，然后也要考虑list为空的情况。
```