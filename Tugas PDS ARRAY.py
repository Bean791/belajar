print("SELAMAT DATANG DI REKAP NILAI")
b=int(input("Mau masukan berapa banyak orang "))
# ini untuk yang multydimensi
data=[[],[],[]]
# ini untuk yang 1 dimensi
pernyataan=["Lulus","Gagal","Nyaris"]
for i in range(b):
    nama=input("nama anda ")
    Kelas=input("masukan kelas anda ")
    nilai=int(input("masukan nilai anda "))
    data[0].append(nilai)
    data[1].append(nama)
    data[2].append(Kelas)
    print("="*50)
    print("Laporan Nilai")
    if nilai > 75:
        hasil=print("Selamat Anda",pernyataan[0])
    elif nilai == 75:
        hasil=print("Selamat Anda",pernyataan[2])
    elif nilai < 75:
        hasil=print("Selamat Anda ",pernyataan[1])
    print("Untuk ",nama)
    print("ada di kelas ", Kelas)
    print(" dengan nilai ",nilai)
    print("="*50)
print("="*50)
print("Rangkuman")
for h in range(len(data) ):
    print(data[h])
      