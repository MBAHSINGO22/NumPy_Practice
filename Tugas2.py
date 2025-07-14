import numpy as np

suhu = np.array([26, 27, 25, 30, 29, 25, 28])
kelembapan = np.array([60, 70, 65, 65, 70, 75, 80])
x = np.mean(suhu)
y = np.mean(kelembapan)
b1 = (np.sum((suhu - x) * (kelembapan - y)) / np.sum((suhu - x) ** 2))
b0 = y - b1 * x
suhuHari8 = 27
prediksiKelembapan = b0 + b1 * suhuHari8
print("Prediksi cuaca pada hari ke-8 adalah", prediksiKelembapan)
