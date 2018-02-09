"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
"""


def arrange(timeslot):
    timeslot.sort()
    for i in range(len(timeslot)-1):
        if timeslot[i][1] > timeslot[i+1][0]:
            return False
    return True


print(arrange([(0, 5), (5, 10), (15, 20)]))
