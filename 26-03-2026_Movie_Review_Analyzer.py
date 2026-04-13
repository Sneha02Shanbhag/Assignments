from textblob import TextBlob

reviews = [
    "Amazing movie",
    "Very boring film",
    "Good acting but slow",
    "Fantastic experience",
    "Worst movie ever"
]

for r in reviews:
    polarity = TextBlob(r).sentiment.polarity
    sentiment = "Positive" if polarity>0 else "Negative" if polarity<0 else "Neutral"
    print(r, "->", sentiment)
