def solve(s):
    fmx, find = 0, 0
    smx, sind = 0, 0
    n = len(s)
    for i in range(n):
        qutr = int(s[i])
        if qutr > fmx:
            smx = fmx
            sind = find

            fmx = qutr
            find = i
        elif qutr > smx:
            smx = qutr
            sind = i
    acha = kegon(find, s)
    ss = kegon(sind, s)
    ans = 0
    if acha != -1:
        ans = max(ans, fmx * 10 + acha)
    if ss != -1:
        ans = max(ans, smx * 10 + ss)
    return ans


def kegon(ind, s):
    n = len(s)
    acha = -1
    for i in range(ind + 1, n):
        q = int(s[i])
        acha = max(acha, q)
    return acha


tot = 0
while True:
    try:
        a = solve(input())
    except EOFError:
        break
    tot += a
print(tot)
