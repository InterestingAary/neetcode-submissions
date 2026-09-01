class Solution:
    def reverse(self, x: int) -> int:
        n = list(str(x))
        
        if n[0] == '-':
            rev = '-' + ''.join(n[:0:-1])
        else:
            rev = ''.join(n[::-1])
        rev = int(rev)
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        
        return rev
