mat = []
while True:
    try:
        ll = input()
        mat.append(ll)
    except EOFError:
        break
n, m = len(mat), len(mat[0])
ans = 0

drx = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, -1], [-1, 1], [1, 1], [-1, -1]]
inbound = lambda r, c: 0 <= r < n and 0 <= c < m

for i in range(n):
    for j in range(m):
        if mat[i][j] == "@":
            cc = 0
            for r, c in drx:
                nr, nc = r + i, c + j
                if inbound(nr, nc) and mat[nr][nc] == "@":
                    cc += 1
            ans += cc < 4
print(ans)
