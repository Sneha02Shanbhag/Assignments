import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.DataFrame({
 "Income":[15,16,17,18,60,62,65,70,120,130],
 "Spending":[39,81,6,77,50,55,52,60,20,15]
})

k = KMeans(n_clusters=3, random_state=0)
df["Cluster"] = k.fit_predict(df)

print(df.groupby("Cluster").mean())

plt.scatter(df["Income"], df["Spending"], c=df["Cluster"])
plt.xlabel("Income"); plt.ylabel("Spending")
plt.title("Customer Segmentation (K-Means)")
plt.show()

print("Clusters represent low/medium/high value customers.")
