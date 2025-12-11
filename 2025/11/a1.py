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
first = "you"
last = "out"
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
dist[first] = 1
q = deque([first])
while q:
    node = q.popleft()

    for child in graph[node]:
        indegree[child] -= 1
        dist[child] += dist[node]

        if not indegree[child]:
            q.append(child)
print(dist[last])
