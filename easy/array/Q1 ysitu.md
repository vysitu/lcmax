[LINK TO QUESTION](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/)


Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be accepted.

 

Example 1:
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```
Example 2:
```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

Constraints:

- 0 <= nums.length <= 3 * 104
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.

-----
# 解法
- 是有序的数组，所以重复的一定是挨着的
- 重复的是挨着的，所以分两个指针，把后面遇到的重复元素跳过，把有重复的元素的第一个移动到开头就行
- 输出是长度，改过的数组不需要输出

# Python3
```python3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_len = len(nums)  #数组总长度
        p1 = 0              #向前搜索的指针
        p2 = 0              #指向不重复的列表的最后一位的指针
        for p1 in range(num_len-1): 
            p1 +=1          #从第二个元素开始
            if nums[p1] == nums[p2]: 
                nums[p1] = '-'  #消除所有和p2相同的元素
            else:    #向前搜索发现不一样的元素时，移动指针，复制元素，消除前方那个元素
                p2 = p2+1
                nums[p2] = nums[p1] 
                if p2 != p1:   #如果移动到两者重复了，那么不要消除那个元素
                    nums[p1] = '-'
        return(p2+1)  #p2指向最后一位，是从0开始算，求长度要在此基础上+1
```