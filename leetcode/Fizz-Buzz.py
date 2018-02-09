# Fizz Buzz
# write a program that output the string representation of numbers 1 to n
# multiples of three should output Fizz
# 5 should output Buzz
# both 3 and 5's multiples output FizzBuzz


class Solution():

    def FizzBuzz(self, n):

        return_str = []

        for i in range(n+1):
            if i % 15 == 0:
                return_str.append('FizzBuzz')
            elif i % 5 == 0 :
                return_str.append('Buzz')
            elif i % 3 == 0 :
                return_str.append('Fizz')
            else:
                return_str.append(i)
        return return_str


test = Solution()
print(test.FizzBuzz(5))