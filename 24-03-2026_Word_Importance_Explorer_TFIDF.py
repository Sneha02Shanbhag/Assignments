from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

docs = [
    "Machine learning improves systems",
    "AI and machine learning are powerful",
    "Deep learning is part of AI",
    "AI used in healthcare",
    "Technology uses artificial intelligence"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

print("TF-IDF Matrix:\n", df)

print("\nTop Keywords per Document:")
for i,row in df.iterrows():
    print(f"Doc {i+1}:", list(row.sort_values(ascending=False).head(3).index))
