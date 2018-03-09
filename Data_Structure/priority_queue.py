"""
Python使用优先队列代码：
import Queue
q = Queue.PriorityQueue()
q.put(1) #添加元素
q.get()  #删除元素
1
2
3
4
python的优先队列基于最小堆实现。

Heap（堆）是一个除了底层节点外的完全填满的二叉树，底层可以不完全，左到右填充节点。而最小堆意味着，
任一非终端节点的数据值均不大于其左子节点和右子节点的值。如图：

min_heap

"""

"""
import Queue

class ComparableObj:                  # 可比较对象，放入优先队列中
    def __init__(self, **):
        ...

    def __cmp__(self, other):         # 比较规则的指定，谁做根（大顶堆，小顶堆）
                                      # 返回的是布尔类型
        ...
        return True/Flase
        ...

que = Queue.PriorityQueue()

que.put(ComparableObj(**))
que.put(ComparableObj(**))
...

que.qsize()
                # 优先队列中元素的个数

que.get()
                # 返回根（优先队列第一个出队的元素）

"""

# construct priorityQueue by heapq module
from heapq import heappush, heappop


class PriorityQueue:
    def __init__(self):
        self._queue = []

    def put(self, item, priority):
        heappush(self._queue, (priority, item))  # heappush(self._queue, (-priority, item)) 改变pop顺序

    def get(self):
        return heappop(self._queue)


q = PriorityQueue()
q.put('world', 2)
q.put('hello', 1)

"""
>>>q.get()[1]
hello
>>>q.get()[1]
world
"""
