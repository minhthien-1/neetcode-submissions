import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hang_ht = collections.defaultdict(set)
        cot_ht = collections.defaultdict(set)
        khoi_ht = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                so_ht = board[r][c]
                if (so_ht in hang_ht[r]) or (so_ht in cot_ht[c]) or (so_ht in khoi_ht[(r//3,c//3)]):
                    return False
                hang_ht[r].add(so_ht)
                cot_ht[c].add(so_ht)
                khoi_ht[(r//3,c//3)].add(so_ht)
        return True