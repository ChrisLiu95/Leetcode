"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.



Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

"""


def myAtoi(self, str):
    """
    :type str: str
    :rtype: int
    """
    if not str:
        return 0

    index = 0
    total = 0
    sign = 1
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    while str[index] == " " and index < len(str):
        index += 1

    if (str[index] == "+" or str[index] == "-") and index < len(str):
        if str[index] == "+":
            sign = 1
        else:
            sign = -1
        index += 1

    while index < len(str):
        if "0" <= str[index] <= "9":
            digit = int(str[index])
            total = 10 * total + digit
            if total > INT_MAX:
                return INT_MAX if sign == 1 else INT_MIN
            elif total == INT_MAX:
                return INT_MAX if sign == 1 else -INT_MAX
            index += 1
        else:
            break

    return sign * total
