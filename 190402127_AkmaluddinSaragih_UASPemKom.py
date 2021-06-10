print ("Program Pengembalian Uang Kasir dan Pecahan")

a = int (input("Masukkan Jumlah Total Belanja : Rp. "))
b = int (input("Masukkan Uang Pembeli : Rp. "))

kembalian = b-a

print ("Kembaliannya Sebesar Rp. ",kembalian,"dengan Rincian Kembalian ")

satuan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 100, 50]

uang = kembalian

for pecahan in satuan :
    if uang < pecahan :
        continue
    banyak_pecahan = int(uang / pecahan)
    uang = uang - (pecahan * banyak_pecahan)
    print ('pecahan {} : {}' .format(pecahan, banyak_pecahan))
else :
    print ("Tidak Ada")
