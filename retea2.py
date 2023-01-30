# Read function
def read():
    file = open("retea.in")

    # Read number of power plants and houses
    n, m = map(int, file.readline().split())

    # Read power plant coordinates
    for i in range(n):
        x, y = map(int, file.readline().split())
        powers[i] = [x, y]

    # Read houses coordinates
    for i in range(m):
        x, y = map(int, file.readline().split())
        houses[i] = [x, y]

    file.close()
    return n, m


# Function to calculate distance between coordinates
def distance(c1, c2):
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) ** 0.5


# Prim algorithm with heap
def prim(heap):
    visited = [False] * m
    final_cost = 0

    while heap:
        top = heap.pop(0)

        if not visited[top[1]]:
            visited[top[1]] = True
            final_cost += top[0]

            for i in range(m):
                if i != top[1]:
                    old_dist = dist[i]
                    dist[i] = min(dist[i], distance(houses[top[1]], houses[i]))

                    if dist[i] < old_dist:
                        heap.append(dist[i], i)

    return final_cost


powers, houses = {}, {}
n, m = read()
dist, heap = [1e12] * m, []

# Smallest distance between a power plant and a house
for i in range(m):
    for j in range(n):
        dist[i] = min(dist[i], distance(powers[j], houses[i]))

    heap.append([dist[i], i])

# Prim's algorithm
print(prim(heap))
