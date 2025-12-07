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
dis = [[0] * m for _ in range(n)]
dis[0][start] = 1

for row in range(n):
    for col in range(m):
        if dis[row][col]:
            dr, dc = row + down[0], col + down[1]
            if inbound(dr, dc):
                if mat[dr][dc] == ".":
                    dis[dr][dc] += dis[row][col]
                else:
                    lr, lc = dr + left[0], dc + left[1]
                    if inbound(lr, lc):
                        dis[lr][lc] += dis[row][col]
                    rr, rc = dr + right[0], dc + right[1]
                    if inbound(rr, rc):
                        dis[rr][rc] += dis[row][col]


print(sum(dis[-1]))
