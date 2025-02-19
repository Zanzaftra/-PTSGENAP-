import random

def sapa_acak():
    sapaan = ["Assalamualaikum", "Halo", "Selamat pagi"]
    nama = ["teman-teman", "rekan-rekan", "sobat"]
    
    pilihan_sapaan = random.choice(sapaan)
    pilihan_nama = random.choice(nama)

    print(f"{pilihan_sapaan}, {pilihan_nama}! Semangat belajar Python!")

sapa_acak()
#B
# Line 1 =  Mengimpor modul random untuk memilih elemen secara acak.
# line 3 = fungsi untuk mencetak sapaan yang ngacak atau acakan
# line 4 dan 5 itu buat pilihan sapaan dan nama
# line 7 dan 8 itu buat milih salah satu sapaan kalo gak satu nama acak dari line sebelumnya atau dari list yang di atas linenya
# line 10 = buat manggil sapaan yang kepilih di layar
# line terakhir itu agar programnya dijalankan dan buat menghasilkan sapaan yang acak

#C
# 1. NIGMPORMODUL RANDOM BUAT MILIH ELEMEN ACAK 
# 2. buat fungsi "sama_acak()" yang nyimpan 2 list yaitu sapaan dan nama
# 3. milih sapaan dan nama acak pakai random.choice()
# 4. mencetak hasil sapaan yang sudah kita pilih
# 5. manggil fungsi sapa_acak() yang kalau programnya itu dijalankan langsung menunjukkan sapan acaknya