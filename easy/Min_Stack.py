"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""


class Minstack(object):
    def __init__(self):
        self.stack = []
        self.minstack = []

    def __str__(self):
        ss = ""
        for num in self.stack:
            ss += "," + str(num)
        return ss[1:]

    def push(self, x):
        self.stack.append(x)
        if self.minstack:
            if x <= self.minstack[-1]:
                self.minstack.append(x)
        else:
            self.minstack.append(x)

    def pop(self):
        temp = self.stack.pop()
        if self.minstack:
            if temp == self.minstack[-1]:
                self.minstack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minstack[-1]


mystack = Minstack()
mystack.push(-2)
mystack.push(0)
mystack.push(-3)
print(mystack)
print(mystack.getMin())
mystack.pop()
print(mystack)
print(mystack.getMin())
