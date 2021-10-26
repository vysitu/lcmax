[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/)

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:
```
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
```
Example 2:
```
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:
```
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
```

Constraints:

- 1 <= prices.length <= 3 * 104
- 0 <= prices[i] <= 104

-----
# 解法
求一阶“导数”，凡是正的就买，凡是负的就不买
- 输入是一个列表
- 输出是一个数字，即最大能够得到的利益

# Python3
```python3
    price_diff = []
    profit = 0
    for i in range(len(prices)):
        if i>=1:    #从第二个元素开始算导数
            diff = prices[i] - prices[i-1]
            price_diff.append(diff)
    for pd in price_diff:  #len is len(prices)-1
        if pd > 0:  # 价位差为正的话就加到总收益里
            profit = profit+pd
    return(profit)
```