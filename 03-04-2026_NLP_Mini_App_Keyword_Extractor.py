import re
from collections import Counter

text = """Artificial Intelligence is transforming industries. Machine learning and deep learning
are subsets of AI that help in automation, prediction, and decision making."""

words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

stopwords = {"is","and","in","of","that","are","the","a","on","for","to"}
filtered = [w for w in words if w not in stopwords]

freq = Counter(filtered)

print("Top Keywords:")
for word, count in freq.most_common(5):
    print(f"{word} : {count}")

print("\nExplanation: Important words extracted using frequency.")
