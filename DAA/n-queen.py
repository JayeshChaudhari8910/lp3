def n_queens(n):
    col = set()
    posDiag=set() # (r+c)
    negDiag=set() # (r-c)

    res=[]

    board = [["0"]*n for i in range(n) ]
    def backtrack(r):
        if r==n:#current row and all queens are placed
            copy = [" ".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c]="1"

            backtrack(r+1)

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c]="0"
    backtrack(0)
    for sol in res:
        for row in sol:
            print(row)
        print()

n= int(input("Emter no of queens"))
n_queens(n)