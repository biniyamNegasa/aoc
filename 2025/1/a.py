sz = 1
# sz = 10

pp = 50
zeros = 0
for _ in range(sz):
    kk = input()
    fidel, qutr = kk[0], kk[1:]
    qutr = int(qutr)
    prev = pp
    kk = qutr // 100
    zeros += kk
    qutr %= 100
    if fidel == "L":
        pp -= qutr
    else:
        pp += qutr
    zeros += (pp <= 0 or pp >= 100) and prev != 0
    pp %= 100
print(zeros)
