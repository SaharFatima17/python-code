import numpy as np

x = np.array([345, 123, 567, 342, 987])
y = np.array([345000, 123000, 567000, 342000, 987000])

# Means
MeanOfX = np.mean(x)
MeanOfY = np.mean(y)
MeanOfXY = np.mean(x * y)
MeanOfX2 = np.mean(x**2)

# Formula:
# m = (mean(xy) - mean(x)*mean(y)) / (mean(x^2) - mean(x)^2)
# b = mean(y) - m*mean(x)

numerator = MeanOfXY - MeanOfX * MeanOfY
denominator = MeanOfX2 - (MeanOfX ** 2)

m = numerator / denominator     # Corrected (was modulus %)
b = MeanOfY - m * MeanOfX

print("Slope (m):", m)
print("Intercept (b):", b)

# Predict for x = 567
answer = m * 567 + b
print("Final Answer:", answer)
