import matplotlib.pyplot as plt
import pandas as pd

# Data dummy sederhana
data = {
    'Hari': ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat'],
    'Penjualan': [120, 150, 180, 90, 200]
}

df = pd.DataFrame(data)

# Bikin grafik
plt.figure(figsize=(8,5))
plt.plot(df['Hari'], df['Penjualan'], marker='o', linewidth=2, markersize=8)
plt.title('Penjualan Mingguan Toko ABC', fontsize=16)
plt.xlabel('Hari')
plt.ylabel('Jumlah Penjualan')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()