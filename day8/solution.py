import numpy as np


with open("input_small.txt", "r") as f:
    lines = f.read().splitlines()

boxes = []
for i, line in enumerate(lines):
    boxes.append([int(elem) for elem in line.split(",")])

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



# Part 1: connect up to 1000 boxes into clusters

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


# Part 2
# xxx