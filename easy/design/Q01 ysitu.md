[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/)




Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
 

Example 1:
```
Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                       // Any permutation of [1,2,3] must be equally likely to be returned.
                       // Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]
```
 

Constraints:
```
1 <= nums.length <= 200
-106 <= nums[i] <= 106
All the elements of nums are unique.
At most 5 * 104 calls in total will be made to reset and shuffle.
```

-----
# 解法
想不到吧！（我没想到
import random 就可以了！
random.shuffle(list1) 会直接原位shuffle list1，不返回值。
copy是python自带的一个库，可以完成深度拷贝。用这个可以避免改变一个列表的时候另一个列表受到影响。

# Python3 
```python3
import random
from copy import deepcopy as dc
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = dc(nums)
        self.work = dc(nums)

    def reset(self) -> List[int]:
        self.work = dc(self.nums)
        return(self.work)

    def shuffle(self) -> List[int]:
        random.shuffle(self.work)
        return(self.work)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

Runtime: 394 ms         (23.03%)
Memory Usage: 19.4 MB   (72.35%)
```