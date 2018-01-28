# function to reverse an array in groups


def reverse_group(input, k):
    start = 0
    result = []
    while start < len(input):
        if len(input[start:]) < k:
            result = result + list(reversed(input[start:]))
            break
        result = result + list(reversed(input[start:start+k]))
        start = start + k
    return result


input = [1, 2, 3, 4, 5, 6, 7]
print(reverse_group(input, 3))
