# UBAH SESUAI KEBUTUHAN UNTUK MENGUBAH DATA SESUAI SOAL VARIASI KARENA INI VARIASI 5B

mean = 72000000
sd = 9000000
sp1 = 36
sp2 = 100

# SOAL A
se_36 = sd / (sp1 ** 0.5)
print(f"Standar Error of Sample Mean (Soal A) = {se_36:.3f}")

# SOAL B
se_100 = sd / (sp2 ** 0.5)
print("\nDengan n = 100, menurut CLT, distribusi sampling mean mendekati normal dengan mean = 72000000 dan sd = se_100")
print("CLT menjamin bahwa rata-rata sampel akan terdistribusi normal jika ukuran sampel cukup besar (biasanya n > 30) dan observasi independen serta varians populasi terbatas")

# SOAL C
z = (76500000 - mean) / se_36
print("\nZ-Score (Soal C) =", z)

# SOAL D
print("\nDistribusi rata-rata sampel cenderung mendekati distribusi normal meskipun distribusi populasi awal tidak normal karena adanya CLT")
print("CLT menyatakan bahwa jika ukuran sampel cukup besar, maka distribusi dari rata-rata sampel akan mendekati distribusi normal dengan mean sama dengan mean populasi dan simpangan baku")
print("Secara intuitif, ketika kita mengambil rata-rata dari banyak data acak, penyimpangan nilai ekstrem akan saling meniadakan, sehingga rata-rata cenderung berada di sekitar mean populasi")
print("Selain itu, hal tersebut juga membentuk pola simetris seperti kurva lonceng (bell curve) yang merupakan karakteristik dari distribusi normal")
print("Oleh karena itu, semakin besar ukuran sampel, semakin kecil pengaruh data ekstrem, dan distribusi rata-rata sampel akan semakin mendekati distribusi normal")