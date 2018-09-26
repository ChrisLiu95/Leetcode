# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75
# }
#
# # for key in prices:
# #     print(key, prices[key])
# #
# #  dictionary eliminate duplication
# # a = {1, 2, 3, 4, 4, 4, 4, 5}
# # for i in a:
# #     print(i)
#
# min_price = min(zip(prices.values(), prices.keys()))
# max_price = max(zip(prices.values(), prices.keys()))
# prices_sorted = sorted(zip(prices.values(), prices.keys()), reverse=True)
#
# # print(min_price)
# # print(max_price)
# # print(prices_sorted)
#
# a = {
#     'x': 1,
#     'y': 2,
#     'z': 3
# }
# b = {
#     'w': 10,
#     'x': 11,
#     'y': 2
# }
#
# # Find keys in common
# print(a.keys() & b.keys())  # { 'x', 'y' }
# # Find keys in a that are not in b
# print(a.keys() - b.keys())  # { 'z' }
# # Find (key,value) pairs in common
# print(a.items() & b.items())  # { ('y', 2) }
from operator import itemgetter

#
# rows = [
#     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
#     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
#     {'fname': 'Bzg', 'lname': 'Jones', 'uid': 1004}
# ]
#
# rows_by_fname = sorted(rows, key=lambda r: r['fname'])  # looks better, by using lambda
# rows_by_uid = sorted(rows, key=itemgetter('uid'))
# print(rows_by_fname)
# print(rows_by_uid)

# However, the solution involving itemgetter() typically runs a bit faster.
# Thus, you might prefer it if performance is a concern.


"""
Last, but not least, don’t forget that the technique shown in this recipe can be applied to functions such as min() and max(). For example:
>>> min(rows, key=itemgetter('uid'))
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001} >>> max(rows, key=itemgetter('uid'))
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004} >>>
"""
#
# rows = [
#     {'address': '5412 N CLARK', 'date': '07/01/2012'},
#     {'address': '5148 N CLARK', 'date': '07/04/2012'},
#     {'address': '5800 E 58TH', 'date': '07/02/2012'},
#     {'address': '2122 N CLARK', 'date': '07/03/2012'},
#     {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
#     {'address': '1060 W ADDISON', 'date': '07/02/2012'},
#     {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
#     {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
# ]
# from operator import itemgetter
# from itertools import groupby
#
# # Sort by the desired field first
# rows.sort(key=lambda x: x['date'])
# # Iterate in groups
# for date, items in groupby(rows, key=itemgetter('date')):
#     print(date)
#     for i in items:
#         print(' ', i)

# values = ['1', '2', '-3', '-', '4', 'N/A', '5']
#
#
# def is_int(val):
#     try:
#         x = int(val)
#         return True
#     except ValueError:
#         return False
#
#
# ivals = list(filter(is_int, values))
# print(ivals)

#   addresses = [
#     '5412 N CLARK',
#     '5148 N CLARK',
#     '5800 E 58TH',
#     '2122 N CLARK'
#     '5645 N RAVENSWOOD',
#     '1060 W ADDISON',
#     '4801 N BROADWAY',
#     '1039 W GRANVILLE',
# ]
# counts = [0, 3, 10, 4, 1, 7, 6, 1]
#
# """
# >>> from itertools import compress
# >>> more5 = [n > 5 for n in counts]
# >>> more5
# [False, False, True, False, False, True, True, False] >>> list(compress(addresses, more5))
#     ['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']
#     >>>
# """

# Determine if any .py files exist in a directory
# import os
#
# files = os.listdir("/Users/Lxc/Desktop/cv")
# if any(name.endswith('.py') for name in files):
#     print('There be python!')
# else:
#     print('Sorry, no python.')
# # Output a tuple as CSV
# s = ('ACME', 50, 123.45)
# print(','.join(str(x) for x in s))

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
# string matching
from fnmatch import fnmatchcase

str1 = [addr for addr in addresses if fnmatchcase(addr, '* ST')]

str2 = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]

print(str1, str2)
