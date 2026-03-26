import matplotlib.pyplot as plt

sales = [10,20,35,50,65]
labels = ["A","B","C","D","E"]

plt.figure()
plt.bar(labels, sales)
plt.title("Bar: Category Sales")
plt.xlabel("Category"); plt.ylabel("Sales")
plt.show()

plt.figure()
plt.pie(sales, labels=labels, autopct="%1.1f%%")
plt.title("Pie: Share")
plt.show()

plt.figure()
plt.hist(sales, bins=5)
plt.title("Histogram: Distribution")
plt.show()

print("Story: Sales steadily increase from A to E, with E dominating the share.")
