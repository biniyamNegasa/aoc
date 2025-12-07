jj = input().split(",")
mx = 0
for i in range(len(jj)):
    jj[i] = list(map(int, jj[i].split("-")))
ans = 0
lst = set()
MX = 100000
for i in range(1, MX):
    curr = int(str(i) * 2)
    while len(str(curr)) < 11:
        lst.add(curr)
        curr = int(str(curr) + str(i))
for v in lst:
    for l, r in jj:
        if l <= v <= r:
            ans += v
print(ans)
