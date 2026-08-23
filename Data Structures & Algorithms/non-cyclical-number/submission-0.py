class Solution:
    def isHappy(self, n: int) -> bool:
        # base case
        if n == 1:
            return True
        if n == 4:
            return False
        sum2 = 0
        temp = n
        while temp > 0:
            digit = temp % 10
            sum2 += digit * digit
            temp //= 10

        return self.isHappy(sum2)
