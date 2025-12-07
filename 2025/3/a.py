def solve(s):
    n = len(s)
    pos = 0
    limit = 12
    ind = 0
    ans = []
    for pos in range(limit):
        for i in range(9, 0, -1):
            t = ind
            while t < n - limit + pos + 1 and s[t] != str(i):
                t += 1
            if t < n - limit + pos + 1:
                ans.append(str(i))
                ind = t + 1
                break
    return "".join(ans)


tot = 0
while True:
    try:
        a = solve(input())
    except EOFError:
        break
    vv = int(a)
    tot += int(vv)
print(tot)
