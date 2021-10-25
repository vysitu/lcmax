class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        leftP = 0
        rightP = len(s) - 1

        if len(s) % 2 != 0:
            while leftP != rightP:
                s[leftP], s[rightP] = s[rightP], s[leftP]
                leftP += 1
                rightP -= 1
        else:
            while len(s) // 2 != leftP:
                s[leftP], s[rightP] = s[rightP], s[leftP]
                leftP += 1
                rightP -= 1
