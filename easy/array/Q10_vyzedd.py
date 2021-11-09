class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)
        #assign rows/ columns/ boxes to 9/9/9
        rows = [set() for _ in range(N)]
        columns = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        
        #go over each element in this board, return false if the element alrealy exists in any of it row, column or box
        for r in range(N):
            for c in range(N):
                val = board[r][c]
                
                #if val = '.' then skip 
                if val == '.':
                    continue
                
                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                if val in columns[c]:
                    return False
                columns[c].add(val)
                
                #r//3*3 + c//3 -> the current box number
                index = (r//3)*3 + c//3
                if val in boxes[index]:
                    return False
                boxes[index].add(val)
                
        return True
                
                
