"""
Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =
[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

"""


class solution(object):

    def __init__(self, vector):
        self.vector = vector
        self.i = 0
        self.j = 0

    def next(self):
        temp = self.vector[self.j][self.i]
        self.i = self.i + 1
        return temp

    def hasnext(self):
        while self.j < len(self.vector):
            if self.i < len(self.vector[self.j]):
                return True
            else:
                self.i = 0
                self.j = self.j + 1
        return False


i, v = solution(([1, 2], [3], [4, 5, 6], [3, 2])), []
while i.hasnext():
    v.append(i.next())
print(v)

