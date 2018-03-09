"""
1.栈(stacks)是一种只能通过访问其一端来实现数据存储与检索的线性数据结构，具有后进先出(last in first out，LIFO)的特征

2.队列(queue)是一种具有先进先出特征的线性数据结构，元素的增加只能在一端进行，元素的删除只能在另一端进行。能够增加元素的队列一
端称为队尾，可以删除元素的队列一端则称为队首。


# 关于栈
# >>> stack = [3, 4, 5]
# >>> stack.append(6)
# >>> stack.append(7)
# >>> stack
# [3, 4, 5, 6, 7]
# >>> stack.pop()
# 7
# >>> stack
# [3, 4, 5, 6]
# >>> stack.pop()
# 6
# >>> stack.pop()
# 5
# >>> stack
# [3, 4]
#
# 关于队列
# >>> from collections import deque
# >>> queue = deque(["Eric", "John", "Michael"])
# >>> queue.append("Terry")           # Terry arrives
# >>> queue.append("Graham")          # Graham arrives
# >>> queue.popleft()                 # The first to arrive now leaves
# 'Eric'
# >>> queue.popleft()                 # The second to arrive now leaves
# 'John'
# >>> queue                           # Remaining queue in order of arrival
# deque(['Michael', 'Terry', 'Graham'])

"""


# whether s is a palindrome
def palindrome(s):
    return s == s[::-1]


def palindrome2(s):
    from collections import deque
    deque = deque(s)
    while len(deque) > 1:
        if deque.popleft() != deque.pop():
            return False
    return True


def main():
    print(palindrome2('aba'))


main()
