class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x, y):
        par_x = self.find(x)
        par_y = self.find(y)

        if par_x == par_y:
            return False

        if self.size[par_x] >= self.size[par_y]:
            self.par[par_y] = par_x
            self.size[par_x] += self.size[par_y]
        else:
            self.par[par_x] = par_y
            self.size[par_y] += self.size[par_x]

        return True


def get_input():
    coords = []
    while True:
        try:
            coord = list(map(int, input().strip().split(",")))
            coords.append(coord)
        except EOFError:
            break
    return coords


def get_dist(first, second):
    x1, y1, z1 = first
    x2, y2, z2 = second

    return pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2)


coordinates = get_input()
n = len(coordinates)

distances = []

for i in range(n):
    for j in range(i + 1, n):
        curr_dist = get_dist(coordinates[i], coordinates[j])
        distances.append([curr_dist, i, j])
uf = UnionFind(n)
distances.sort()
limit = 1000
for i in range(min(len(distances), limit)):
    _, first_ind, second_ind = distances[i]
    uf.union(first_ind, second_ind)

sorted_comp = sorted(uf.size, reverse=True)
x, y, z = sorted_comp[:3]
print(x * y * z)
