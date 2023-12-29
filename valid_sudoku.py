def isValidSudoku(board):
    rows = [[] for _ in range(9)]
    columns = [[] for _ in range(9)]
    subbox = [[] for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                num = int(board[i][j])
                if num in rows[i]:
                    return False
                if num in columns[j]:
                    return False
                n = int(i/3)*3+int(j/3)
                if num in subbox[n]:
                    return False
                rows[i].append(num)
                columns[j].append(num)
                subbox[n].append(num)
                
    return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
    