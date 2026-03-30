#
# @lc app=leetcode.cn id=36 lang=python3
# @lcpr version=30204
#
# [36] 有效的数独
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCount = Counter(board[0])
        if max(rowCount.values()) > 1:
            return False
        colCount = Counter([x[0] for x in board])
        if max(colCount.values()) > 1:
            return False
        squareCount = Counter([board[r][c] for r in range(3) for c in range(3)])
        if max(squareCount.values()) > 1:
            return False


# @lc code=end



#
# @lcpr case=start
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

# @lcpr case=start
# [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#

