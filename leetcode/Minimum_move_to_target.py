# use the minimum steps to reach a number from 0, on i-th move,
# you can either move i forward or i steps back


def minimum_move(num):
    num = abs(num)
    my_sum = 0
    step = 0
    while my_sum < num or (my_sum - num) % 2 != 0:
        step = step + 1
        my_sum = my_sum + step
    return step


print(minimum_move(2))
