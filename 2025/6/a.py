from functools import reduce


mat = []
while True:
    try:
        line = input()
        mat.append(line)
    except EOFError:
        break
n = len(mat)
m = len(mat[0])
pp = 0
arr = []
for i in range(len(mat[-1])):
    if mat[-1][i] != " ":
        arr.append(i - pp - 1)
        pp = i
arr.append(len(mat[-1]) - pp)
k = 1
ans = 0
l = 0
while l < m:
    qutrs = []
    for j in range(l + arr[k] - 1, l - 1, -1):
        cc = 0
        for i in range(n - 1):
            if mat[i][j] != " ":
                cc *= 10
                cc += int(mat[i][j])
        qutrs.append(cc)
    if mat[-1][l] == "*":
        ans += reduce(lambda x, y: x * y, qutrs, 1)
    else:
        ans += reduce(lambda x, y: x + y, qutrs, 0)
    l += arr[k] + 1
    k += 1
print(ans)
