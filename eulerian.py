from collections import defaultdict


# Return Eulerian path via DFS
def dfs(x):
    while graph[x]:
        dfs(graph[x].pop())
    ans.append(x)


# Read file
with open("eulerian.in") as file:
    pairs = []
    for f in file:
        pairs.append([int(x) for x in f.split()])


# Build graph and nodes degree
graph, degree = defaultdict(list), defaultdict(int)
for x, y in pairs:
    graph[x].append(y)
    degree[x] += 1
    degree[y] -= 1


# Pick starting node
for k in degree:
    if degree[k] == 1:
        start = k
        break

ans = []
dfs(start)
ans.reverse()

# Print path
print([[ans[i], ans[i+1]] for i in range(len(ans)-1)])
