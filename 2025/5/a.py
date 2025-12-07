from collections import defaultdict

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
lst = defaultdict(int)
for l, r in fresh:
    lst[l] -= 1
    lst[r] += 1
lst = [[k, v] for k, v in lst.items()]
lst.sort()

lv = -1
cc = 0
for val, f in lst:
    cc += f
    if f <= 0 and lv == -1:
        lv = val
    if not cc:
        ans += val - lv + 1
        lv = -1

print(ans)
