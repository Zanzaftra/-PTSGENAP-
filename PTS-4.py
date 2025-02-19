def cek_ganjil_genap(n):
    return "Ganjil" if n % 2 != 0 else "Genap"

print(cek_ganjil_genap(7))
print(cek_ganjil_genap(10))

# JAWABAN B
# line 1 itu buat menjadikan cek_ganjil_genap() nya itu hanya dapat 1 parameter 
# line 2 itu, pakai if else buat nentuiin apakah n nya itu ganjil atau cek_ganjil_genap
# line 4 = manggil fungsi cek_ganjil_genap(7) untuk ngecek 7 itu ganjil atau genap terus di cetak hasilnya
# line 5 = sama seperti line 4 menggil fungsinya dan ngecek apakah 10 itu ganjil atau genap dan dicetak deh hasilnya

# JAWABAN C
# 1. buat fungsi yang mengecek n itu ganjil atau genap pkai modulus
# 2. kalo n habis dibagi 2 maka genap begitupun sebliknya
# 3. programnya manggil fungsi 2 kali, pertama dengan 7 yang ganjil dan kedua yang 10 cek_ganjil_genap