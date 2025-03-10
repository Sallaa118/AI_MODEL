import numpy as np

# Fungsi sederhana: y = x^2
def fungsi_loss(x):
    return x**2

# Gradien (turunan)
def gradien(x):
    return 2 * x

# Gradient Descent
x = 10  # Starting point
learning_rate = 0.1

for i in range(100):
    grad = gradien(x)
    x -= learning_rate * grad

print("Nilai minimum dari fungsi y=x^2 adalah:", x)
