# find the maximum sum of sub-array in a given array


def maximum_sub_array(given_array):
    max_current = max_global = given_array[0]
    for i in range(1, len(given_array)-1):
        max_current = max(given_array[i], max_current + given_array[i])
        if max_current > max_global:
            max_global = max_current
    return max_global


my_array = [-2, 3, 2, -1, 3, -1]
print(maximum_sub_array(my_array))


