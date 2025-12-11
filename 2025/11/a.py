from collections import defaultdict, deque


def get_input():
    graph = defaultdict(list)
    while True:
        try:
            parent, *others = input().strip().split(":")
            children = others[0].strip().split()
            for child in children:
                graph[parent].append(child)
        except EOFError:
            break
    return graph


graph = get_input()
first = "svr"
last = "out"
dac = "dac"
fft = "fft"


def how_many(first, last, ini):
    q = deque([first])
    indegree = defaultdict(int)
    visited = set([first])
    while q:
        node = q.popleft()
        for child in graph[node]:
            indegree[child] += 1
            if child not in visited:
                visited.add(child)
                q.append(child)
    dist = defaultdict(int)
    dist[first] = ini
    q = deque([first])
    while q:
        node = q.popleft()

        for child in graph[node]:
            indegree[child] -= 1
            dist[child] += dist[node]

            if not indegree[child]:
                q.append(child)
    return dist[last]


vv = how_many(fft, last, how_many(dac, fft, how_many(first, dac, 1)))
ww = how_many(dac, last, how_many(fft, dac, how_many(first, fft, 1)))
print(vv + ww)
