from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[500],[800],[1000],[1200]]) # sqft
y = np.array([1500000, 2400000, 3000000, 3600000])

model = LinearRegression().fit(X,y)
pred = model.predict([[900]])
print("Predicted price for 900 sqft:", int(pred[0]))
