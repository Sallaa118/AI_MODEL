import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset sederhana
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 6, 9, 12, 15])

# Membuat model
model = LinearRegression()
model.fit(X, y)

# Prediksi
prediksi = model.predict([[6]])
print("Prediksi untuk input 6:", prediksi)
