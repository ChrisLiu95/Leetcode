"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)


"""


class Solution(object):
    def findIp(self, str):
        if not str or len(str) < 4 or len(str) > 12:
            return -1
        res = []
        index = 0
        ip = ""
        self.dfs(str, index, res, ip)
        return res

    def dfs(self, str, index, res, ip):
        if index == 4:
            if not str:
                res.append(ip[1:])
                return
        for i in range(1, 4):
            if i <= len(str):
                if int(str[:i]) <= 255:
                    self.dfs(str[i:], index + 1, res, ip + "." + str[:i])
                if str[0] == "0":
                    break


test = Solution()
print(test.findIp("23423443"))
