class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFFFFFFF
        sign_bit = 0x80000000

        while b != 0:
            partial_sum = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a, b = partial_sum, carry

        return a if a < sign_bit else a - (1 << 32)
        