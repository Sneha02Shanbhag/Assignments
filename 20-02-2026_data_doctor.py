import pandas as pd

df = pd.DataFrame({
 "Name":["Sneha","Sneha",None,"Rahul"],
 "City":["blr","blr","mys","mys"],
 "Marks":[90,90,None,75]
})

print("Original:\n", df)

df = df.drop_duplicates()
df["Name"] = df["Name"].fillna("Unknown")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["City"] = df["City"].str.upper()

print("\nCleaned:\n", df)
print("\nWhy cleaning? Removes noise, handles missing values, standardizes text → better ML accuracy.")
