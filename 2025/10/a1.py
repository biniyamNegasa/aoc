def get_input():
    testcases = []
    while True:
        try:
            first, *second, third = input().strip().split()
            expected = first[1:-1]
            qutr = 0
            for i in range(len(expected)):
                if expected[i] == "#":
                    qutr ^= 1 << i
            switches = []
            for curr in second:
                lst = list(map(int, curr[1:-1].split(",")))
                cc = 0
                for i in lst:
                    cc ^= 1 << i
                switches.append(cc)

            joltages = list(map(int, third[1:-1].split(",")))
            testcases.append([qutr, switches, joltages])
        except EOFError:
            break
    return testcases


testcases = get_input()
answer = 0
for testcase in testcases:
    expected, togglers, _ = testcase
    n = len(togglers)

    def comb(ind, curr, count):
        if not curr:
            return count
        if ind >= n:
            return float("inf")

        first = comb(ind + 1, curr ^ togglers[ind], count + 1)
        second = comb(ind + 1, curr, count)

        return min(first, second)

    answer += comb(0, expected, 0)
print(answer)
