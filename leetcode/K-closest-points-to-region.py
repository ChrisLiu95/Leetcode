# find  K closest points to the region(0, 0)in a coordinate system
# given a list of tuple/array like [(1,2),(1,-1),(2,3),(4,6)]


class Solution(object):

    def k_closest(self, arr, k):
        distances = []
        for point in arr:
            x = point[0]
            y = point[1]
            distance = (x ** 2 + y ** 2) ** (1 / 2)
            distances.append([distance, point])
        distances.sort(reverse=True)
        return [distances[i][1] for i in range(0, k)]


test = Solution()
print(test.k_closest([(1, 2), (1, -1), (2, 3), (4, 6)], 4))
