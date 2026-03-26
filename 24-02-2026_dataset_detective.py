import pandas as pd

df = pd.DataFrame({
 "A":[1,2,3,4],
 "B":[4,5,None,7],
 "C":[10,20,30,40]
})

print(df.head())
print("\nMax per column:\n", df.max(numeric_only=True))
print("\nMissing values:\n", df.isnull().sum())

print("\nInsights:")
print("1) Column C has highest scale values.")
print("2) Column B has missing values.")
print("3) Data seems small and clean otherwise.")
print("4) Values in A increase linearly.")
print("5) Mean of B can be used to fill missing.")
