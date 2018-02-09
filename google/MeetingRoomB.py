"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.


time interval:
|                 |      
   |  |   |   |

start:
|  |      |
      |       |   |
end.sort:
"""


def meetingroomb(interval):
    start = []
    end = []
    for item in interval:
        start.append(item[0])
        end.append(item[1])
    start.sort()
    end.sort()

    e = 0
    res = 0

    for i in range(len(interval)):
        if start[i] < end[e]:
            res = res + 1
        else:
            e = e + 1
    return res


print(meetingroomb([(0, 30), (5, 10), (5, 20)]))




