"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
return 964176192 (represented in binary as 00111001011110000010100101000000).



"""


class Solution(object):
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #given 32 bits unsigned integer
        oribin = '{0:032b}'.format(n)
        print(oribin)
        temp = oribin[::-1]
        return int(temp, 2)


test = Solution()
print(test.reverseBits(1))
