# two sum problem
# num_list[1,2,3,4,56], target=12
# two_sum[num_list,target] --> False
# three different ways to solve this problem : o(n^2), o(n log n), o(n)


def two_sum_n_square(num_list, target):
    length = len(num_list)
    for i in range(length):
        for j in range(length):

            value = num_list[i]+num_list[j]

            if value == target and i != j:
                return True

    return False


print(two_sum_n_square([1, 2, 3], 2))


def two_sum_n_log_n(num_list, target):

    num_list.sort()
    length = len(num_list)

    left_index = 0
    right_index = length - 1

    while left_index < right_index:

        value = num_list[left_index]+num_list[right_index]

        if value == target:
            return True
        elif value > target:
            right_index -= 1
        else:
            left_index += 1

    return False


print(two_sum_n_log_n([1, 2, 3], 2))


def two_sum_n(num_list, target):

    already_seen = set()

    for number in num_list:
        value = target - number

        if value in already_seen:
            return True
        else:
            already_seen.add(number)

    return False


print(two_sum_n([1, 2, 3], 4))
