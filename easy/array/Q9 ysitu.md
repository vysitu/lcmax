[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```
Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
 ```

Constraints:
```
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 ```

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

-----
# 解法
双循环很明显可以解决这个问题，但是我们可以尝试更巧妙的办法。      
如果解是a+b=c，将所有的值都减去和c，那么a和b将得到-b和-a。因为只有一组解，减去c再取反之后得到的列表和之前的应该只有a和b是相同的。     

# Python3
```python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n2 = nums.copy()
        singular_ind = []
        for i in range(len(nums)):
            if n2[i] == target/2.0:   # 如果两个解是一样的，就要单独处理一下
                singular_ind.append(i)
                if len(singular_ind) == 2:  # 出现两次1/2的解，就可以提交
                    return(singular_ind)
            n2[i] = -1*(n2[i] - target)
        solution = set(n2).intersection(set(nums))  # 取交集
        if len(solution)==3:
            solution.remove(target/2)
        solindex = []
        for i in solution:
            solindex.append(nums.index(i))
        return(solindex)

Runtime: 68 ms
Memory Usage: 16.2 MB



## 顶级理解我都有点看不懂在干嘛，这不还是循环了两次吗
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i, num in enumerate(nums):
            numberToFind = target-num
            if numsMap.get(numberToFind) is not None:
                return [numsMap.get(numberToFind), i]

            numsMap[num] = i
            
        return None

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        
        for i in range(len(nums)):
            if target - nums[i] in complement:
                return [complement[target - nums[i]], i]
            
            complement[nums[i]] = i
```