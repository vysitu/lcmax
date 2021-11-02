class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        res = []
        for i in digits:
            s += str(i)
            
        temp = int(s) + 1
        
        s_1 = str(temp)
        
        for i in s_1:
            res.append(int(i))
            
        return res
        
        
