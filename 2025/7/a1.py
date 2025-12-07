from collections import deque

mat = []
while True:
    try:
        line = input().strip()
        mat.append(line)
    except EOFError:
        break
n, m = len(mat), len(mat[0])

down = [1, 0]
left, right = [0, -1], [0, 1]
inbound = lambda r, c: 0 <= r < n and 0 <= c < m

start = -1
for j in range(m):
    if mat[0][j] == "S":
        start = j
        break
q = deque([(0, start)])
vis = [[0] * m for _ in range(n)]
vis[0][start] = 1
cc = 0

while q:
    row, col = q.popleft()

    if mat[row][col] == ".":
        nr, nc = row + down[0], col + down[1]
        if inbound(nr, nc) and not vis[nr][nc]:
            q.append((nr, nc))
            vis[nr][nc] = 1
    else:
        cc += 1
        nr, nc = row + left[0], col + left[1]
        if inbound(nr, nc) and not vis[nr][nc]:
            q.append((nr, nc))
            vis[nr][nc] = 1
        nr, nc = row + right[0], col + right[1]
        if inbound(nr, nc) and not vis[nr][nc]:
            q.append((nr, nc))
            vis[nr][nc] = 1
print(cc)
