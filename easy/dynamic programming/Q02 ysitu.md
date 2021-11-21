[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/)



You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```
Example 2:
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 ```

Constraints:
```
1 <= prices.length <= 105
0 <= prices[i] <= 104
```

-----
# 解法
尝试了很久，从一开始双循环到后来多次取整个数列的最大最小值，最后看了网友的代码才想清楚。
双循环应该是O(n^2)了，相比之下只循环一次，搞两个指针，用蠕动的方法，其实之前的题目里面我也搞过，但是这次一直没有想清楚。

# Python3
```python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        head = 1
        tail = 0
        profit = 0
        while head <= len(prices)-1:
            if prices[head]>prices[tail]:
                profit = max([prices[head]-prices[tail], profit])
            else:
                tail = head
            head += 1
        return(profit)

Runtime: 1569 ms            (10.44%)
Memory Usage: 25.2 MB       (11.60%)
```