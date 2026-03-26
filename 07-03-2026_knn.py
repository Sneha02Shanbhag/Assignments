from sklearn.neighbors import NearestNeighbors
import numpy as np

# toy user-item vectors
X = np.array([[5,3,0],[4,0,0],[1,1,0],[0,0,5]])
model = NearestNeighbors(n_neighbors=2).fit(X)

query = np.array([[5,2,0]])
dist, idx = model.kneighbors(query)
print("Nearest users:", idx)
print("Interpretation: Recommend items liked by similar users.")
