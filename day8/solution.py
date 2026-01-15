import numpy as np


with open("input_small.txt", "r") as f:
    lines = f.read().splitlines()

boxes = []
for i, line in enumerate(lines):
    boxes.append(tuple(int(elem) for elem in line.split(",")))

print(boxes[0])

def euclidean_dist3d(pointA, pointB):
    return np.sqrt((int(pointB[0]) - int(pointA[0]))**2 + (int(pointB[1]) - int(pointA[1]))**2 + (int(pointB[2]) - int(pointA[2]))**2)


def calc_distances(boxes):
    """Calculate all distances and sort them in ascending order"""
    num_boxes = len(boxes)
    distances = []
    for a in range(num_boxes - 1):
        for b in range(a+1, num_boxes):
            distance = euclidean_dist3d(boxes[a], boxes[b])
            distances.append((boxes[a], boxes[b], distance))
    
    distances.sort(key= lambda x: x[2])
    return distances



# Part 1: connect up to 1000 boxes into clusters (naive)
distances = calc_distances(boxes)

clusters = []
for distance in distances[:10]:
    pointA, pointB, _ = distance
    pointA, pointB = tuple(pointA), tuple(pointB)
    
    # Find which clusters contain these points
    cluster_indices = []
    for i, cluster in enumerate(clusters):
        if pointA in cluster or pointB in cluster:
            cluster_indices.append(i)
    
    if len(cluster_indices) == 0:
        # Neither point in any cluster
        clusters.append({pointA, pointB})
    elif len(cluster_indices) == 1:
        # One point in a cluster, add the other
        clusters[cluster_indices[0]].add(pointA)
        clusters[cluster_indices[0]].add(pointB)
    else:
        # Both in different clusters, merge them
        merged = clusters[cluster_indices[0]].union(clusters[cluster_indices[1]])
        clusters[cluster_indices[0]] = merged
        clusters.pop(cluster_indices[1])

clusters.sort(key=lambda x:len(x), reverse=True)
print(clusters[:5])
print("Final result:", len(clusters[0]) * len(clusters[1]) * len(clusters[2]))


# Part 1: Use disjoint-set data structure (smart)
class UnionFind():
    def __init__(self, elements):
        self.parent = {elem: elem for elem in elements}
        self.rank = {elem: 0 for elem in elements}

    def find(self, x):
        if self.parent[x] != x:
            # Iterate through tree till root and set parent of x directly to root (path compression)
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        # Both points already have the same root => same cluster already
        if px == py:
            return
        # If py is taller than px (higher rank), then add px to py, otherwise the other way around
        if self.rank[px] < self.rank[py]:
            py, px = px, py
        self.parent[py] = px
        # Only increase the rank (height), if both trees had the same rank, so the rank naturally increases
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1


uf = UnionFind(set(tuple(box) for box in boxes))

for pointA, pointB, _ in distances[:10]:
    uf.union(pointA, pointB)

clusters = {}
# For each point, get it's root and add the point to the root set in the clusters dict
for point in uf.parent:
    root = uf.find(point)
    if root not in clusters:
        clusters[root] = set()
    clusters[root].add(point)
clusters = list(clusters.values())

clusters.sort(key=lambda x:len(x), reverse=True)
print(clusters)
print("Final result:", len(clusters[0]) * len(clusters[1]) * len(clusters[2]))


