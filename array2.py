data=[[],["Lulus","Gagal","Nyaris"]]
nama=input("nama anda")
Kelas=input("masukan kelas anda")
nilai=int(input("masukan nilai anda"))
data[0].append(nilai)
print("="*50)
print("Laporan Nilai")
if nilai > 75:
    hasil=print("Selamat Anda",data[1][0])
elif nilai == 75:
    hasil=print("Selamat Anda",data[1][2])
elif nilai < 75:
    hasil=print("Selamat Anda ",data[1][1])
print("Untuk ",nama)
print("ada di kelas ", Kelas)
print(" dengan nilai ",data[0][0])
print("="*50)
