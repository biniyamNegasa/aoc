from collections import deque


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

q = deque()
dis = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if mat[i][j] == "@":
            cc = 0
            for r, c in drx:
                nr, nc = r + i, c + j
                if inbound(nr, nc) and mat[nr][nc] == "@":
                    cc += 1
            if cc < 4:
                q.append((i, j))
            else:
                dis[i][j] = cc
while q:
    row, col = q.popleft()
    ans += 1

    for r, c in drx:
        nr, nc = r + row, c + col
        if inbound(nr, nc) and mat[nr][nc] == "@" and dis[nr][nc] >= 4:
            dis[nr][nc] -= 1

            if dis[nr][nc] < 4:
                q.append((nr, nc))

print(ans)
