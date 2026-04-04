from sklearn.linear_model import LinearRegression
import numpy as np

# Data
X = np.array([1, 2, 3]).reshape(-1, 1)
y = np.array([3, 6, 9])

# Model banana
model = LinearRegression()
model.fit(X, y)

# Prediction
pred = model.predict(X)

print("Predictions:", pred)
print("Slope (Coefficient):", model.coef_)
print("Intercept:", model.intercept_)
