#"abcdefghijklmnopqrstuvwxyz0123456789" are alphabet letters.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s) == 1 or len(s) == s.count(' '):
            return True
        
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        new_string = ''
        
        for i in s.lower():
            if i in alphabet:
                new_string += i.lower()
                
        pointer_1 = 0
        pointer_2 = len(new_string) - 1
        
        while pointer_1 <= pointer_2:
            if new_string[pointer_1] == new_string[pointer_2]:
                pointer_1 += 1
                pointer_2 -= 1
                
            else:
                return False
            
        return True

#Maybe better using Python lambda (filter and map) functions
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        new_string = list(map(lambda ch: ch.lower(), filtered_chars))
                
        if new_string == new_string[::-1]:
            return True
        else:
            return False
