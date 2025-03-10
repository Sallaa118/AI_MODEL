import torch
import torch.nn as nn
import torch.optim as optim

# Definisi model neural network
class TwoLayerNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(TwoLayerNN, self).__init__()
        self.hidden = nn.Linear(input_size, hidden_size)
        self.output = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.hidden(x))
        x = self.output(x)
        return x

# Dataset dummy (dengan dtype agar konsisten)
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]], dtype=torch.float32)
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]], dtype=torch.float32)

# Hyperparameter
input_size = 1
hidden_size = 5
output_size = 1

# Inisialisasi model, loss function, dan optimizer
model = TwoLayerNN(input_size, hidden_size, output_size)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.005)  # Learning rate lebih kecil

# Training loop (meningkatkan epoch untuk akurasi lebih baik)
for epoch in range(2000):  
    optimizer.zero_grad()
    output = model(X)
    loss = criterion(output, y)
    loss.backward()
    optimizer.step()

# Prediksi dengan input 5 (tanpa gradien)
input_test = torch.tensor([[5.0]], dtype=torch.float32)
prediksi = model(input_test).detach().numpy()

print("Prediksi untuk input 5:", prediksi)
