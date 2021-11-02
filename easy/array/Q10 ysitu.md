[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/)

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:

```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```
Example 2:
```
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 ```

Constraints:
```
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
```

-----
# 解法
这个题卡了我一些时间，主要是因为不想把解法写死，然后也懒得硬写……     
检测重复元素的方法有很多，我用的取集合，然后计算元素数量。取行、列或者方形区域的集合之后，应该是“.”（点）加上单独元素。     
——如果没有重复，单独元素的数量加上点的数量，减去重复的一个点（集合里面也包含一个点），应该是9。      
至于取3x3区域的值，我实验之后感觉把所有的行拼成一个列表，再按一定规律取其中的元素，就可以得到需要的slice。

# Python3
```python3
blist = []
shift = []
for i in range(9):
    blist.extend(board2[i])
    count1 = board[i].count('.') + len(set(board[i])) - 1
    shift.append(i*9)
    if count1 < 9:
        print(False)
        break

for i in range(9):
    collist = []
    for shiftval in shift:
        collist.append(blist[i+shiftval])
    count2 = collist.count('.') + len(set(collist)) - 1
    if count2 < 9:
        print(False)
        break    

block = [0,1,2,9,10,11,18,19,20]    #硬解，把位移量算进去
for startpoint in [0,3,6,27,30,33,54,57,60]:
    square = []
    for blockpart in block:
        square.append(blist[startpoint+blockpart])
    count3 = square.count('.') + len(set(square)) - 1
    if count3 < 9:
        print(False)
        break   

Runtime: 84 ms          (99.33%)  #这个成绩我还是非常自豪的！
Memory Usage: 14.2 MB   (89.08%)  #内存占用也小
```