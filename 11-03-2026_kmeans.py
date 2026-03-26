from sklearn.cluster import KMeans
import numpy as np

X = np.array([[100,20],[120,25],[300,70],[320,65]])
k = KMeans(n_clusters=2, random_state=0).fit(X)
print("Labels:", k.labels_)
print("Centers:", k.cluster_centers_)
