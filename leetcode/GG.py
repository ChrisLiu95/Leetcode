"""
TagName tag_name
{} - {} / [] / s

把字典里所有 TagName 转化为 tag_name
TagName --> tag_name

"""


def dfs(s):
    for key, val in s.items():
        index = 0
        for i, j in enumerate(key):
            if 'A' <= j <= 'Z':
                index += 1
                if index == 2:
                    key.lower()
                    key = key[::i] + "_" + key[i::]
        if type(val) == 'list' or type(val) == 'string':
            continue
        dfs(val)
