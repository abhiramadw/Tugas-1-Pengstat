# CARI KALIMAT UBAH SESUAI KEBUTUHAN UNTUK MENGUBAH DATA SESUAI SOAL VARIASI

import matplotlib.pyplot as plt

# Ubah sesuai kebutuhan yaa
data = [51.7, 52.9, 50.5, 51.3, 52.1, 51.5, 53.3, 51.8, 52.3, 53.0, 51.5, 50.7, 53.1, 52.4, 51.5, 50.5,
51.8, 52.3, 53.0, 52.3, 51.2, 51.6, 51.7, 52.0]

freq = {}

for x in data:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print("\nTabel Frekuensi")
print("-" * 40)
print("Nilai\t\tFrekuensi")
print("-" * 40)
for k,v in sorted(freq.items()):
    print(f"{k}\t\t{v}")
print("-" * 40)
print(f"Total\t\t{sum(freq.values())}")

total_freq = sum(freq.values())
print(f"\nTotal frekuensi: {total_freq}")
print(f"Jumlah raw score: {sum(data)}")
print(f"Rata-rata data: {sum(data)/len(data):.3f}")

sorted_data = sorted(data)
n = len(sorted_data)
if n % 2 == 0:
    median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
else:
    median = sorted_data[n//2]

print(f"Median data: {median:.3f}")

max_freq = max(freq.values())
semua_modus = [k for k,v in freq.items() if v == max_freq]
print(f"Modus data: {semua_modus} dengan frekuensi {max_freq}")

if len(semua_modus) > 1:
    print("Distribusi simetris")
else:
    if sum(data)/len(data) > median:
        print("Positively skewed")
    else:
        print("Negatively skewed")

# Tabel Proporsi
print("\nTabel Proporsi")
print("-" * 50)
print("Nilai\t\tFrekuensi\tProporsi")
print("-" * 50)
for k,v in sorted(freq.items()):
    print(f"{k}\t\t{v}\t\t{(v/total_freq):.3f}")
print("-" * 50)

# Ubah sesuai kebutuhan yaa
# Tabel Persentase untuk nilai > 52.1
print("\nTabel Persentase (Nilai > 52.1)")
print("-" * 50)
print("Nilai\t\tFrekuensi\tPersentase")
print("-" * 50)
for k,v in sorted(freq.items()):
    if k > 52.1:
        print(f"{k}\t\t{v}\t\t{(v/total_freq*100):.3f}%")
print("-" * 50)

# Ubah interval sesuai kebutuhan yaa
print("\nTabel Distribusi Frekuensi Berkelompok (interval 0.8)")
print("-" * 35)
print("Kelas\t\tFrekuensi")
print("-" * 35)

# Ubah interval sesuai kebutuhan yaa
intervals = [
    (50.5, 51.3),
    (51.4, 52.2),
    (52.3, 53.1),
    (53.2, 54.0)
]

for bawah, atas in intervals:
    freq = sum(1 for x in data if bawah <= x <= atas)
    if freq > 0:
        print(f"{bawah:.1f}-{atas:.1f}\t{freq}")

print("-" * 35)
print(f"Total\t\t{len(data)}")

# Ubah interval sesuai kebutuhan yaa
# Membuat data baru dengan mengganti 51.2 menjadi 53.1
data_baru = [53.1 if x == 51.2 else x for x in data]

# Ubah interval sesuai kebutuhan yaa
# Mengaplikasikan transformasi (x*2 + 10) pada setiap data
data_transform = [x*2 + 10 for x in data_baru]

# Ubah interval sesuai kebutuhan yaa
# Tabel Transformasi Data
print("\nTabel Transformasi Data")
print("-" * 60)
print("Original\t51.2→53.1\t(x*2 + 10)")
print("-" * 60)
for i in range(len(data)):
    print(f"{data[i]}\t\t{data_baru[i]}\t\t{data_transform[i]}")
print("-" * 60)
print(f"Rata-rata:\t{sum(data)/len(data):.3f}\t\t{sum(data_transform)/len(data_transform):.3f}")

# Menghitung rata-rata baru
print(f"Jumlah data setelah transformasi: {len(data_transform)}")
print(f"Rata-rata data setelah transformasi (x*2 + 10): {sum(data_transform)/len(data_transform):.3f}")

# Histogram
plt.figure(figsize=(10, 6))
kelas = [f"{bawah:.1f}-{atas:.1f}" for bawah, atas in intervals]
frekuensi = [sum(1 for x in data if bawah <= x <= atas) for bawah, atas in intervals]

plt.bar(kelas, frekuensi)
plt.title('Histogram Distribusi Frekuensi')
plt.xlabel('Kelas Interval')
plt.ylabel('Frekuensi')
plt.xticks(rotation=45)

# Menambahkan nilai frekuensi di atas bar
for i, v in enumerate(frekuensi):
    plt.text(i, v, str(v), ha='center', va='bottom')

plt.tight_layout()
plt.show()