class Solution:
    row = 0
    col = 0
    total = 0

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.total = self.row * self.col

        lp = 0
        rp = self.total - 1
        while lp <= rp:
            m = lp + (rp - lp)// 2
            midx = matrix[self.getIdx(m)[0]][self.getIdx(m)[1]]
            lpidx = matrix[self.getIdx(lp)[0]][self.getIdx(lp)[1]]
            rpidx = matrix[self.getIdx(rp)[0]][self.getIdx(rp)[1]]

            if target < midx:
                rp = m - 1
            elif target > midx:
                lp = m + 1
            else:
                return True
        return False


    def getIdx(self,idx : int) -> tuple[int]:
        if idx < self.col:
            return (0,idx)
        else:
            temp_row = idx // self.col
            return (temp_row, idx - (temp_row * self.col))