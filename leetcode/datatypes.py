# list
my_list = [1, 2, 3, 4, 5]
# for i in my_list:
#    print(i)

# tuple
my_tuple = (1, 2, 3, 4, 5)
# for i in my_tuple:
#    print(i)

# dictionary
my_dic = {
    '0': '_',
    '1': None,
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}
for key, val in my_dic.items():
    print('my {} is {}'.format(key, val))

# set
my_set = {1, 2, 2, 3, 3, 4, 5}
# for i in my_set:
#    print(i)  will delete the duplicated number in the set
