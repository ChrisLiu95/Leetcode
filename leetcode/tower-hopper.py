class Solution(object):
    def __init__(self, tower):
        self.tower = tower

    def whether_go_out(self):
        current = 0
        while True:
            if current >= len(self.tower):
                return True
            if self.tower[current] == 0:
                return False
            current = self.next_step(current)

    def next_step(self, index):
        temp_list = []
        if index + self.tower[index] >= len(self.tower):
            return index+self.tower[index]
        else:
            for i in range(index+1, index+self.tower[index]+1):
                temp_list.append(i + self.tower[i])
            return temp_list.index(max(temp_list))+index+1


test = Solution([4, 0, 0, 1, 0, 0])
print(test.whether_go_out())
