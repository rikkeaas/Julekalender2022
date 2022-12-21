from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
import numpy as np

#Adapted from: https://stackoverflow.com/questions/62376042/calculating-and-displaying-a-convexhull

points = np.ndarray((500,2))
f = open("data.txt", 'r')
for i,ns in enumerate(f.readlines()):
    n1,n2 = ns.split()
    points[i,] = [float(n1), float(n2)]

hull = ConvexHull(points)
print(hull.volume)
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 3))

for ax in (ax1, ax2):
    ax.plot(points[:, 0], points[:, 1], '.', color='k')
    if ax == ax1:
        ax.set_title('Given points')
    else:
        ax.set_title('Convex hull')
        for simplex in hull.simplices:
            ax.plot(points[simplex, 0], points[simplex, 1], 'c')
        ax.plot(points[hull.vertices, 0], points[hull.vertices, 1], 'o', mec='r', color='none', lw=1, markersize=10)
    ax.set_xticks(range(10))
    ax.set_yticks(range(10))
plt.show()