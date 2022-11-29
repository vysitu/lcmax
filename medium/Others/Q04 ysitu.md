[Link to Question](https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/826/)




Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
```
Example 2:
```
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
```
Example 3:
```
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 ```

Constraints:
```
1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
```

-----
# 解法
每个任务的进行就像游戏放技能需要冷却（CD）。    
给每个单独的任务类型建立“数量”和“CD”两个记录，然后在迭代中选择最合适的任务，并维护那两个记录。    

我用的是比较传统的思路，创建字典让两条记录跟着任务走。

这个方法需要注意的东西：
1. 每一轮都要减少所有任务的CD，并且注意不要出现负值
2. 如果全部CD都不是0，那么就进入idle状态
3. 重点：每一轮都要从CD最少的那些元素（都是0）里面选数量最多的那个元素，优先把数量多的任务做掉。
4. 因为全部CD都不是0就会进入idle状态，所以第三点里面CD最少的元素其CD肯定是0，不需要额外判断。
5. 一个任务类型全部完成之后就从三个列表中都把这个任务对应的数据删掉

优化成全部列表操作可能会稍微快些。

# Python3
```python3
def tasker2(tasks, n):
    '''
    变量优先，三个表分别是 元素，数量，冷却时间
    tasks: something like ['a','b','c','a','b','c']
    n: cooldown time for the same task
    '''
    elem_unique = list(set(tasks))  #后面会删去其中元素，所以不要直接用这个变量
    task_dict = {
        'elem':elem_unique,
        'count':[0]*len(elem_unique),
        'cd':[0]*len(elem_unique)
    }
    for e in tasks:
        task_dict['count'][elem_unique.index(e)]+=1
        
    output = []
    count = 0
    
    while max(task_dict['count'])>0:
        count += 1
        # print(f'step {count}')
        # print(task_dict)

        # 全体 cd减少1 ，如果全部都在CD，跳过后面步骤并且记录'idle'状态
        new_cd_list = []
        for cd in task_dict['cd']:
            new_cd = 0 if cd-1 < 0 else cd-1
            new_cd_list.append(new_cd)
        task_dict['cd'] = new_cd_list
        if min(task_dict['cd']) > 0:
            output.append('idle')
            continue
            
        # 选择cd最小的元素里面数量最多的，经过上面筛选，目前肯定有元素cd完毕
        take_elem_ind = min(range(len(task_dict['cd'])), key=task_dict['cd'].__getitem__)
        for ind, e in enumerate(task_dict['elem']):
            if task_dict['cd'][ind] == 0:
                if task_dict['count'][take_elem_ind] < task_dict['count'][ind]:
                    take_elem_ind = ind
        take_elem = task_dict['elem'][take_elem_ind]
        output.append(take_elem)
        task_dict['cd'][take_elem_ind] = n+1

        # 用完了就移除
        if task_dict['count'][take_elem_ind]-1 == 0:
            task_dict['elem'].pop(take_elem_ind)
            task_dict['count'].pop(take_elem_ind)
            task_dict['cd'].pop(take_elem_ind)
        else:
            task_dict['count'][take_elem_ind] -= 1
        
        if len(task_dict['count'])==0:
            break
        
    return len(output)

速度很慢（3300+ms），占用内存15.5MB（16%）
```