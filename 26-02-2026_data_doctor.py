# Extended cleaning with duplicates, case normalization and type casting
import pandas as pd

df = pd.DataFrame({
 "name":["sneha","Sneha","RAHUL","rahul"],
 "marks":["90","90","80","80"],
 "city":["blr","BLR","mys","MYS"]
})

print("Original:\n", df)

df = df.drop_duplicates()
df["name"] = df["name"].str.title()
df["city"] = df["city"].str.upper()
df["marks"] = df["marks"].astype(int)

print("\nCleaned:\n", df)
