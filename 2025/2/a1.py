jj = input().split(",")
mx = 0
for i in range(len(jj)):
    jj[i] = list(map(int, jj[i].split("-")))
ans = 0
for i in range(100000):
    curr = int(str(i) * 2)
    for l, r in jj:
        if l <= curr <= r:
            ans += curr
print(ans)
