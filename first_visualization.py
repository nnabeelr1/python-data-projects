import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data yang lebih realistis dan menarik
data = {
    'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 
              'Jul', 'Ags', 'Sep', 'Okt', 'Nov', 'Des'],
    'Penjualan_Online': [15000, 18000, 22000, 25000, 28000, 32000,
                        35000, 38000, 42000, 45000, 50000, 55000],
    'Penjualan_Offline': [12000, 14000, 16000, 18000, 20000, 22000,
                         25000, 27000, 30000, 32000, 35000, 40000],
    'Target': [20000, 22000, 25000, 28000, 30000, 33000,
              36000, 39000, 42000, 45000, 48000, 52000]
}

df = pd.DataFrame(data)

# Setup style yang lebih keren
plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
fig.patch.set_facecolor('#0e1117')

# === GRAFIK 1: Line Chart Multi-Series ===
ax1.plot(df['Bulan'], df['Penjualan_Online'], 
         marker='o', linewidth=3, markersize=8, 
         color='#00ff88', label='Online Sales', 
         markerfacecolor='white', markeredgecolor='#00ff88', markeredgewidth=2)

ax1.plot(df['Bulan'], df['Penjualan_Offline'], 
         marker='s', linewidth=3, markersize=8, 
         color='#ff6b35', label='Offline Sales',
         markerfacecolor='white', markeredgecolor='#ff6b35', markeredgewidth=2)

ax1.plot(df['Bulan'], df['Target'], 
         marker='^', linewidth=2, markersize=7, 
         color='#ffd23f', linestyle='--', label='Target',
         markerfacecolor='white', markeredgecolor='#ffd23f', markeredgewidth=2)

ax1.fill_between(df['Bulan'], df['Penjualan_Online'], alpha=0.3, color='#00ff88')
ax1.fill_between(df['Bulan'], df['Penjualan_Offline'], alpha=0.2, color='#ff6b35')

ax1.set_title('📈 Performa Penjualan Tahunan 2024', 
              fontsize=18, fontweight='bold', color='white', pad=20)
ax1.set_xlabel('Bulan', fontsize=14, color='white')
ax1.set_ylabel('Penjualan (Rp)', fontsize=14, color='white')
ax1.grid(True, alpha=0.3, color='gray', linestyle='-', linewidth=0.5)
ax1.legend(loc='upper left', fontsize=12, framealpha=0.9, 
           facecolor='black', edgecolor='white')

# Formatting angka di Y-axis
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'Rp{x/1000:.0f}K'))
ax1.set_facecolor('#1e1e1e')

# === GRAFIK 2: Bar Chart Comparison ===
x = np.arange(len(df['Bulan']))
width = 0.35

bars1 = ax2.bar(x - width/2, df['Penjualan_Online'], width, 
                label='Online Sales', color='#00ff88', alpha=0.8, 
                edgecolor='white', linewidth=1)
bars2 = ax2.bar(x + width/2, df['Penjualan_Offline'], width, 
                label='Offline Sales', color='#ff6b35', alpha=0.8,
                edgecolor='white', linewidth=1)

# Tambah nilai di atas bar
for bar in bars1:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 500,
             f'{height/1000:.0f}K', ha='center', va='bottom', 
             color='white', fontweight='bold', fontsize=10)

for bar in bars2:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 500,
             f'{height/1000:.0f}K', ha='center', va='bottom', 
             color='white', fontweight='bold', fontsize=10)

ax2.set_title('📊 Perbandingan Online vs Offline Sales', 
              fontsize=18, fontweight='bold', color='white', pad=20)
ax2.set_xlabel('Bulan', fontsize=14, color='white')
ax2.set_ylabel('Penjualan (Rp)', fontsize=14, color='white')
ax2.set_xticks(x)
ax2.set_xticklabels(df['Bulan'])
ax2.legend(loc='upper left', fontsize=12, framealpha=0.9,
           facecolor='black', edgecolor='white')
ax2.grid(True, alpha=0.3, axis='y', color='gray', linestyle='-', linewidth=0.5)
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'Rp{x/1000:.0f}K'))
ax2.set_facecolor('#1e1e1e')

# Tambah info statistik
total_online = df['Penjualan_Online'].sum()
total_offline = df['Penjualan_Offline'].sum()
growth_online = ((df['Penjualan_Online'].iloc[-1] - df['Penjualan_Online'].iloc[0]) / 
                 df['Penjualan_Online'].iloc[0] * 100)

# Tambah text box dengan statistik
stats_text = f"""
📈 INSIGHTS 2024:
• Total Online Sales: Rp{total_online/1000000:.1f}M
• Total Offline Sales: Rp{total_offline/1000000:.1f}M
• Online Growth: +{growth_online:.1f}%
• Best Month: {df.loc[df['Penjualan_Online'].idxmax(), 'Bulan']}
"""

fig.text(0.02, 0.02, stats_text, fontsize=11, color='#00ff88', 
         bbox=dict(boxstyle="round,pad=0.5", facecolor='black', 
                  edgecolor='#00ff88', alpha=0.8))

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)
plt.show()

# Bonus: Save grafik sebagai file
plt.savefig('sales_analysis_2024.png', dpi=300, bbox_inches='tight', 
            facecolor='#0e1117', edgecolor='none')
print("🎉 Grafik berhasil disimpan sebagai 'sales_analysis_2024.png'")
print("💡 Tips: File gambar juga bisa di-upload ke GitHub untuk portfolio!")