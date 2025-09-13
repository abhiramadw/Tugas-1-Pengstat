# UBAH SESUAI KEBUTUHAN UNTUK MENGUBAH DATA SESUAI SOAL VARIASI KARENA INI VARIASI 3D

data = [62, 77, 68, 83, 55, 91, 74, 66, 80, 72, 88, 59, 93, 71, 64, 85, 79, 58, 87, 69]

mean = sum(data)/len(data)
print(f"Mean adalah {mean:.3f} dengan sum data {sum(data)} dan jumlah data {len(data)}")
ss = 0
for x in range(len(data)):
    ss += (data[x]-mean)**2
    print(f"Iterasi ke-{x} adalah ({data[x]}-{mean})^2 = {(data[x]-mean)**2:.3f}")

print(f"\nSum of Squares adalah {ss}")

variance = ss/len(data)

print(f"Variance adalah {variance:.3f}")

standar_deviasi = variance**0.5

print(f"Standar Deviasi adalah {standar_deviasi:.3f}")