"""
评测题目: 给定登入登出的cookieid,+行为类型,+行为时间的log，得到分小时的在线人数
[cookieid:122,status:login/logout, time:17:00]

时间复杂度： O(N) N为userlog中的条数
"""


class Solution(object):
    def counthour(self, userlog):
        if not userlog:
            return 0
        mydir = {}
        userlog = sorted(userlog, key=lambda x: (x[0], x[2]))  # 先按照ID排序，然后按照时间
        i = 0
        lastest = max([item[2] for item in userlog])  # 所有时间中最晚的那个

        while i < len(userlog):
            if i + 1 < len(userlog) and userlog[i + 1][0] == userlog[i][0]:  # 用户登录并且登出
                for j in range(int(userlog[i + 1][2][:2]) - int(userlog[i][2][:2]) + 1):  # 每个时间段区间，时间加1
                    mydir[str(int(userlog[i][2][:2]) + j)] = mydir.get(str(int(userlog[i][2][:2]) + j), 0) + 1
                i += 2
            else:  # 用户一直处于登录状态， 则每个时间段都加1
                for j in range(int(lastest[:2]) - int(userlog[i][2][:2]) + 1):
                    mydir[str(int(userlog[i][2][:2]) + j)] = mydir.get(str(int(userlog[i][2][:2]) + j), 0) + 1
                i += 1
        return mydir


test = Solution()
print(
    test.counthour([[3, "login", "17:00"], [2, "login", "17:00"], [1, "login", "18:00"], [1, "logout", "18:20"],
                    [2, "logout", "19:20"], [3, "logout", "19:20"], [4, "login", "14:20"]]))
