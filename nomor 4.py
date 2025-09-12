# UBAH SESUAI KEBUTUHAN UNTUK MENGUBAH DATA SESUAI SOAL VARIASI KARENA INI VARIASI 4B

total = 3000
premium = 800
standard = 1500
basic = 700

# Soal A
premium_tidak_selesai = 20/100*premium
standard_tidak_selesai = 50/100*standard
basic_tidak_selesai = 80/100*basic
total_tidak_selesai = premium_tidak_selesai + standard_tidak_selesai + basic_tidak_selesai
total_premium_standard = premium_tidak_selesai + standard_tidak_selesai
probabilitas_a = total_premium_standard / total_tidak_selesai

print(f"Probabilitas (Soal A) = {probabilitas_a:.3f}")

# Soal B

# Ambil 3 dari 3000
kombinasi_total = (3000 * 2999 * 2998) // (3 * 2 * 1)

# Untuk 1 dari n, kombinasinya adalah n itu sendiri
kombinasi_premium = premium  # 1 dari 800 = 800
kombinasi_standard = standard  # 1 dari 1500 = 1500
kombinasi_basic = basic  # 1 dari 700 = 700

total_kemungkinan = kombinasi_basic * kombinasi_standard * kombinasi_premium

probabilitas_b = total_kemungkinan / kombinasi_total

print(f"Probabilitas (Soal B) = {probabilitas_b:.3f}")

# Soal C

# Premium
base_prob_prem = 25/100
premium_selesai = 80/100*premium # 640 orang
peluang_sertifikat_cepat_premium = base_prob_prem + (40/100*base_prob_prem) # 35%
jumlah_prem_cepat = peluang_sertifikat_cepat_premium * 70/100*premium_selesai # 156.8 orang
jumlah_prem_normal = base_prob_prem * 30/100*premium_selesai # 48 orang
total_prem = jumlah_prem_cepat + jumlah_prem_normal # 204.8 orang

# Standard
base_prob_standard = 15/100
standard_selesai = 50/100*standard # 750 orang
peluang_sertifikat_cepat_standard = base_prob_standard + (40/100*base_prob_standard) # 21%
jumlah_standard_cepat = peluang_sertifikat_cepat_standard * 45/100*standard_selesai # 70.9 orang
jumlah_standard_normal = base_prob_standard * 55/100*standard_selesai # 61.9 orang
total_standard = jumlah_standard_cepat + jumlah_standard_normal # 132.8 orang

# Basic
base_prob_basic = 8/100
basic_selesai = 20/100*basic # 140 orang
peluang_sertifikat_cepat_basic = base_prob_basic + (40/100*base_prob_basic) # 11.2%
jumlah_basic_cepat = peluang_sertifikat_cepat_basic * 30/100*basic_selesai # 4.7 orang
jumlah_basic_normal = base_prob_basic * 70/100*basic_selesai # 7.8 orang
total_basic = jumlah_basic_cepat + jumlah_basic_normal # 12.5 orang

total_sertifikat = total_prem + total_standard + total_basic # 350.1 orang
probabilitas_c = total_sertifikat / total
print(f"Probabilitas (Soal C) = {probabilitas_c:.3f}") 