#membuat fungsi
def salam():
    print ("Hello, Selamat Pagi")

##Pemanggilan fungsi (alt+shift+bawah copy kebwah) (jika ingin buka folder dlm folder cd + nama folder)
salam()
salam()
salam()

#Membuat fungsi dengan parameter
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print ("Luas segitiga: %f" % luas)
#persegi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

#pemanggilan fungsi
luas_segitiga(4, 6)

#persegi
print ("Luas persegi: %d" % luas_persegi(6))
#rumus persegi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi 
    return volume
sisi = 5
print ("Luas persegi:", volume_persegi(sisi))
print ("Volume Kubus:", volume_persegi(sisi))
print ("Luas persegi:", luas_persegi(sisi))

#membuat variabel global
nama = "Belajar Kode"
versi = "1.0.0"

def help():
    #ini variabel lokal
    nama = "Proramku"
    versi = '1.0.1'
    #mengakses variabel lokal
    print ("Nama: %s" % nama)
    print ("Versi: %s" % versi)
#mengakses variabel global
print ("Nama: %s" % nama)
print ("Versi: %s" % versi)

#memanggil fungsi help()
help()
