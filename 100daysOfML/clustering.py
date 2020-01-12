import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans


X = np.array([[1,1],
              [1,2],
              [2,1],
              [4,4],
              [4,5],
              [6,6],
              [3,3]]) #input data

# plt.scatter(X[:,0],X[:,1],s=150)
# plt.show()


clf = KMeans(n_clusters=2) #decide number of cluster centers
clf.fit(X)

centroids = clf.cluster_centers_
labels = clf.labels_

colors = ["g*","r.","c.","b."]

for i in range(len(X)):
    plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize =20)
plt.scatter(centroids[:,0],centroids[:,1], marker="x",s=150, linewidths=5)

plt.show()

