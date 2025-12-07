mat = []
while True:
    try:
        line = input().strip()
        mat.append(list(filter(lambda x: x, line.split())))
    except EOFError:
        break
mat[0], mat[-1] = mat[-1], mat[0]
n = len(mat)
m = len(mat[0])
ans = 0
for j in range(m):
    f = 0
    cc = 0
    if mat[0][j] == "*":
        f = 1
        cc = 1
    for i in range(1, n):
        if f:
            cc *= int(mat[i][j])
        else:
            cc += int(mat[i][j])
    ans += cc
print(ans)
