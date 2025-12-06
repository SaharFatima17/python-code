import numpy as np

# ----- Dataset -----
x = np.array([8, 9, 10, 11, 12])          # Experience in years
y = np.array([15000, 20000, 30000, 40000, 50000])  # Salary in thousands

# ---------------- Step 1: Numerator ----------------
xy = x * y
print("Multiplication of x and y:", xy)

mean_xy = np.mean(xy)
print("Mean of (x*y):", mean_xy)

mean_x = np.mean(x)
print("Mean of x:", mean_x)

mean_y = np.mean(y)
print("Mean of y:", mean_y)

mult_of_means = mean_x * mean_y
print("Multiplication of mean(x) and mean(y):", mult_of_means)

numerator = mean_xy - mult_of_means
print("Numerator value:", numerator)

# ---------------- Step 2: Denominator ----------------
x_square = x**2
print("Square of x:", x_square)

mean_x_square = np.mean(x_square)
print("Mean of x^2:", mean_x_square)

square_mean_x = mean_x**2
print("Square of mean(x):", square_mean_x)

denominator = mean_x_square - square_mean_x
print("Denominator value:", denominator)

# ---------------- Step 3: Slope ----------------
m = numerator / denominator
print("Slope (m):", m)

# ---------------- Step 4: Intercept ----------------
b = mean_y - m * mean_x
print("Intercept (b):", b)

# ---------------- Step 5: Predictions ----------------
def predict(exp):
    return m * exp + b

salary_7 = predict(7)
salary_10 = predict(10)
salary_0 = predict(0)

print("Predicted salary for 7 years:", salary_7)
print("Predicted salary for 10 years:", salary_10)
print("Predicted salary for 0 years:", salary_0)