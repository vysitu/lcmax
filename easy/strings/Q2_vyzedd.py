class Solution:
    def reverse(self, x: int) -> int:
        if x < pow(-2, 31) or x > pow(2, 31) -1:
            return 0
        
        st = str(x)
        
        if x >= 0:
            temp = int(st[::-1])
        else:
            st_1 = st[1:]
            st_2 = st_1[::-1]
            temp = int('-' + st_2)
        
        if temp < pow(-2, 31) or temp > pow(2, 31) -1:
            return 0
        
        return temp
