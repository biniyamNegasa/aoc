fresh = []
available = []
f = 0
mx = 0
while True:
    try:
        kk = input().strip()
        if not kk:
            f = 1
        elif f:
            a = int(kk)
            available.append(a)
            mx = max(mx, a)
        else:
            left, right = map(int, kk.split("-"))
            mx = max(mx, right)
            fresh.append([left, right])
    except EOFError:
        break
ans = 0
for fruit in available:
    for left, right in fresh:
        if left <= fruit <= right:
            ans += 1
            break
print(ans)
